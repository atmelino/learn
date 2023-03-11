import { remultFresh } from "remult/remult-fresh";
import { Task } from "../model/task.ts";
import { createPostgresConnection } from "https://deno.land/x/remult/postgres.ts";

/* configuration sammy */
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


