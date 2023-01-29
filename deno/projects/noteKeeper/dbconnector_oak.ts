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
  //ctx.response.body = "Received a GET HTTP method";
  console.log("dbconnector_oak.ts GET");
  // Run the query
  const result = await client.queryArray`
 SELECT * FROM todos
`;
  console.log("result");
  console.log(result);

  ctx.response.body = JSON.stringify(result.rows);

  // Encode the result as JSON
  //const body = JSON.stringify(result.rows, null, 2);
});

router.post("/todos", async (ctx) => {
  console.log("dbconnector_oak.ts POST");

  const reqBody = await (await ctx.request.body({ type: "json" })).value;
  console.log(reqBody);
  console.log(reqBody.SQL.note);

  //Insert the new todo into the database
  const SQL = `INSERT INTO todos (noteId,note) VALUES ('` + reqBody.SQL.noteId +
    `','` + reqBody.SQL.note + `')`;
  //const SQL = `INSERT INTO todos (noteId,note) VALUES (${reqBody})`;
  // these SQL statements work:
  //INSERT INTO todos (id,noteId,note) VALUES (5,'asdf','rew')
  //INSERT INTO todos (noteId,note) VALUES ('asdf','rew')
  console.log(SQL);

  // await client.queryObject`
  // INSERT INTO todos () VALUES (${reqBody})
  // `;

  await client.queryObject(SQL);

  ctx.response.body = "Received a POST HTTP method";
});

router.put("/", (ctx) => {
  ctx.response.body = "Received a PUT HTTP method";
});

router.delete("/", (ctx) => {
  ctx.response.body = "Received a DELETE HTTP method";
});

app.use(router.allowedMethods());
app.use(router.routes());

app.addEventListener("listen", () => {
  console.log(`Listening on: localhost:${port}`);
});

await app.listen({ port });
