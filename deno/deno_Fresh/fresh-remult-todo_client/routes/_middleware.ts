import { remultFresh } from "remult/remult-fresh";
import { Task } from "../model/task.ts";
import { createPostgresConnection } from "https://deno.land/x/remult/postgres.ts";

//configuration sammy
export const remultServer = remultFresh({
  entities: [Task],
  dataProvider: async () => {
    return createPostgresConnection({
      configuration: {
        user: "postgres",
        password: "password",
        database: "sammy",
        hostname: "localhost",
        port: 5432,
        tls: {enabled:false}
      },
    });
    return await undefined;
  },
}, Response);
export const handler = remultServer.handle;


// configuration atmelino
// export const remultServer = remultFresh({
//   entities: [Task],
//   dataProvider: async () => {
//     return createPostgresConnection({
//       configuration: {
//         hostname: "localhost",
//         port: "5432",
//         user: "atmelino",
//         password: "password",
//         database: "at_data",
//       },
//     });
//     return await undefined;
//   },
// }, Response);
// export const handler = remultServer.handle;

// original
// export const remultServer = remultFresh({
//   entities: [Task],
//   dataProvider: async () => {
//     const dbUrl = Deno.env.get("DATABASE_URL");
//     if (dbUrl) {
//       return createPostgresConnection({ connectionString: dbUrl });
//     }
//     return await undefined;
//   },
// }, Response);
// export const handler = remultServer.handle;
