import { serve } from "https://deno.land/std@0.114.0/http/server.ts";
import * as postgres from "https://deno.land/x/postgres@v0.14.2/mod.ts";
import { Client } from "https://deno.land/x/postgres@v0.17.0/mod.ts";
// password for supabase is deno1pass2word3
// connection string: postgres://postgres:deno1pass2word3@db.lwbjwhxdyxafkxjdldmn.supabase.co:6543/postgres



// Connect to the database
const client = new Client({
  user: "postgres",
  password: "password",
  database: "sammy",
  hostname: "localhost",
  port: 5432,
});
await client.connect();

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
  await client.end();
}

serve(async (req) => {
  console.log(req);

  // Parse the URL and check that the requested endpoint is /todos. If it is
  // not, return a 404 response.
  const url = new URL(req.url);
  if (url.pathname !== "/todos") {
    return new Response("Not Found", { status: 404 });
  }

  await client.connect();

  try {
    console.log("try");
    switch (req.method) {
      case "GET": { // This is a GET request. Return a list of all todos.
        console.log("GET");
        // Run the query
        const result = await client.queryArray`
          SELECT * FROM todos
        `;
        console.log(result);

        // Encode the result as JSON
        const body = JSON.stringify(result.rows, null, 2);

        // Return the result as JSON
        return new Response(body, {
          headers: { "content-type": "application/json" },
        });
      }
      case "POST": { // This is a POST request. Create a new todo.
        // Parse the request body as JSON. If the request body fails to parse,
        // is not a string, or is longer than 256 chars, return a 400 response.
        const title = await req.json().catch(() => null);
        if (typeof title !== "string" || title.length > 256) {
          return new Response("Bad Request", { status: 400 });
        }

        // Insert the new todo into the database
        await client.queryObject`
          INSERT INTO todos (title) VALUES (${title})
        `;

        // Return a 201 Created response
        return new Response("", { status: 201 });
      }
      default: // If this is neither a POST, or a GET return a 405 response.
        return new Response("Method Not Allowed", { status: 405 });
    }
  } catch (err) {
    console.error(err);
    // If an error occurs, return a 500 response
    return new Response(`Internal Server Error\n\n${err.message}`, {
      status: 500,
    });
  } finally {
    // Release the connection back into the pool
    await client.end();
  }
});
