import { useRef, useState } from "preact/hooks";
import { Client } from "https://deno.land/x/mysql@v2.11.0/mod.ts";
import settings from "../../../../../settings.js";
import { Button } from "../components/Button.tsx";

export function dbRead() {
  const [dbread, setdbRead] = useState("database");

  async function init() {
    const client = await new Client().connect({
      hostname: settings.dbsettings.hostname,
      username: settings.dbsettings.username,
      db: settings.dbsettings.db,
      poolSize: settings.dbsettings.poolSize, // connection limit
      password: settings.dbsettings.password,
    });
  }

  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {
        <div>
          <Button onClick={() => init()}>debug message</Button>

          <textarea
            class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
          >
            {dbread}
          </textarea>
        </div>
      }
    </div>
  );
}

// import { Client } from "https://deno.land/x/mysql@v2.11.0/mod.ts";
// import settings from "../../../../../settings.js";

// const client = await new Client().connect({
//   hostname: settings.dbsettings.hostname,
//   username: settings.dbsettings.username,
//   db: settings.dbsettings.db,
//   poolSize: settings.dbsettings.poolSize, // connection limit
//   password: settings.dbsettings.password,
// });

// async function read_database() {
//   const query = `select * from ` + settings.dbsettings.table;
//   const users = await client.query(query);
//   //const users = await client.query(`select * from table1`);
//   console.log(users);

//   await client.close();
// }
