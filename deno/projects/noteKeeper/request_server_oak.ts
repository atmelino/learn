import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import { Client } from "https://deno.land/x/postgres@v0.17.0/mod.ts";
import { oakCors } from "https://deno.land/x/cors/mod.ts";
//import settings from "../../../../../settings.js";

async function createTable() {
  try {
    // Create the table
    const result = await client.queryArray`
  CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
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
  user: "postgres",
  password: "password",
  database: "sammy",
  hostname: "localhost",
  port: 5432,
});
await client.connect();

// const client = await new Client().connect({
//   hostname: settings.dbsettings.hostname,
//   username: settings.dbsettings.username,
//   db: settings.dbsettings.db,
//   poolSize: settings.dbsettings.poolSize, // connection limit
//   password: settings.dbsettings.password,
// });



//createTable();

const port = 8000;
const app = new Application();
app.use(oakCors({ origin: "*" }));

const router = new Router();

router.get("/todos", async (ctx) => {
  //ctx.response.body = "Received a GET HTTP method";
  console.log("GET");
  // Run the query
  const result = await client.queryArray`
 SELECT * FROM todos
`;
  console.log(result);

  ctx.response.body = JSON.stringify(result.rows);

  // Encode the result as JSON
  //const body = JSON.stringify(result.rows, null, 2);
});

router.post("/todos", async (ctx) => {
  const reqBody = await (await ctx.request.body({ type: "json" })).value;
  console.log(reqBody);

  //Insert the new todo into the database
  await client.queryObject`
  INSERT INTO todos (title) VALUES (${reqBody})
`;

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
