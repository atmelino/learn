import { Client } from "https://deno.land/x/mysql/mod.ts";
import settings from './settings.js'

const client = await new Client().connect({
  hostname: "127.0.0.1",
  username: "sammy",
  db: "sammydb",
  poolSize: 3, // connection limit
  password: "",
});

const users = await client.query(`select * from table1`);
console.log(users);

await client.close();