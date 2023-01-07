import { Client } from "https://deno.land/x/mysql/mod.ts";
import settings from '../../../../settings.js'

const client = await new Client().connect({
  hostname: settings.dbsettings.hostname,
  username: settings.dbsettings.username,
  db: settings.dbsettings.db,
  poolSize: settings.dbsettings.poolSize, // connection limit
  password: settings.dbsettings.password,
});

const query=`select * from `+settings.dbsettings.table;
const users = await client.query(query);
//const users = await client.query(`select * from table1`);
console.log(users);

await client.close();

