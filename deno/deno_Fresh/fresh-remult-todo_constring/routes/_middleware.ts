import { remultFresh } from "remult/remult-fresh";
import { Task } from "../model/task.ts";
import { createPostgresConnection } from "https://deno.land/x/remult/postgres.ts";

export const remultServer = remultFresh({
  entities: [Task],
  dataProvider: async () => {
    //const dbUrl = Deno.env.get("DATABASE_URL");
    const dbUrl = "postgres://postgres:password@localhost:5432/at_data";
    if (dbUrl) {
      return createPostgresConnection({ connectionString: dbUrl });
    }
    return await undefined;
  },
}, Response);

export const handler = remultServer.handle;