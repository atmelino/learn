import { Client } from "https://deno.land/x/mysql/mod.ts";

const client = await new Client().connect({
  hostname: "45.79.28.148",
  username: "sammy",
  db: "sammydb",
  poolSize: 3, // connection limit
  password: "password",
});

const users = await client.query(`select * from users`);
console.log(users);

await client.close();
