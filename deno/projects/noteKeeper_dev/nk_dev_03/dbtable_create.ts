import { Client } from "https://deno.land/x/postgres@v0.17.0/mod.ts";
import settings from "../../../../../settings_nk.js";

async function createTable() {
  try {
    // Create the table
    const result = await client.queryArray`
  CREATE TABLE IF NOT EXISTS notes (
    id UUID PRIMARY KEY,
    timestamp TIMESTAMP NOT NULL,
    note TEXT NOT NULL
  )
  `;
    console.log(result);
  } finally {
    // Release the connection back into the pool
    await client.end();
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


