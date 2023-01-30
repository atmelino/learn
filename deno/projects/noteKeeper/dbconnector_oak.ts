import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import { Client } from "https://deno.land/x/postgres@v0.17.0/mod.ts";
import { oakCors } from "https://deno.land/x/cors/mod.ts";
import settings from "../../../../settings_nk.js";

async function createTable() {
  try {
    // Create the table
    const result = await client.queryArray`
  CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    noteId TEXT NOT NULL,
    note TEXT NOT NULL
  )
  `;
    console.log(result);
  } finally {
    // Release the connection back into the pool
    //await client.end();
  }
}

// Connect to the database
const client = new Client({
  user: settings.dbsettings.user,
  password: settings.dbsettings.password,
  database: settings.dbsettings.database,
  hostname: settings.dbsettings.hostname,
  port: settings.dbsettings.port,
});
await client.connect();

createTable();

const port = 7000;
const app = new Application();
app.use(oakCors({ origin: "*" }));

const router = new Router();

router.get("/todos", async (ctx) => {
  console.log("dbconnector_oak.ts GET");
  // Run the query
  const result = await client.queryArray`
 SELECT * FROM todos
`;
  console.log("result");
  console.log(result);

  ctx.response.body = JSON.stringify(result.rows);
});

router.post("/todos", async (ctx) => {
  console.log("dbconnector_oak.ts POST");

  const reqBody = await (await ctx.request.body({ type: "json" })).value;
  console.log(reqBody);
  console.log(reqBody.SQL.note);

  //Insert the new todo into the database

  const sstart = `INSERT INTO todos (timestamp,noteId,note) VALUES ('`;
  const spart1 = reqBody.SQL.timestamp;
  const spart2 = `','`;
  const spart3 = reqBody.SQL.noteId;
  const spart4 = `','`;
  const spart5 = reqBody.SQL.note;
  const send = `')`;
  const SQL = sstart + spart1 + spart2 + spart3 + spart4 + spart5 + send;
  console.log(SQL);
  await client.queryObject(SQL);

  ctx.response.body = "Received a POST HTTP method";
});

router.put("/", (ctx) => {
  ctx.response.body = "Received a PUT HTTP method";
});

router.delete("/todos", async (ctx) => {
  console.log("dbconnector_oak.ts DELETE");
  const reqBody = await (await ctx.request.body({ type: "json" })).value;
  console.log(reqBody);

  const sstart = `DELETE FROM todos WHERE noteid = '`;
  const spart1 = reqBody.SQL.noteId;
  const send = `'`;
  const SQL =sstart+spart1+send;
  console.log(SQL);
  await client.queryObject(SQL);

  ctx.response.body = "Received a DELETE HTTP method";
});

app.use(router.allowedMethods());
app.use(router.routes());

app.addEventListener("listen", () => {
  console.log(`Listening on: localhost:${port}`);
});

await app.listen({ port });

// these SQL statements work:
//INSERT INTO todos (id,noteId,note) VALUES (5,'asdf','rew')
//INSERT INTO todos (noteId,note) VALUES ('asdf','rew')
//INSERT INTO todos (date, time,noteId,note) VALUES ('1999-01-08','040506','asdf','rew')
//DELETE FROM todos WHERE noteid = 'g4YJeL2jVF';
