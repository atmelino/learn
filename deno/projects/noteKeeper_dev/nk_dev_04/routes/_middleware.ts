import { remultFresh } from "remult/remult-fresh";
import { Note } from "../model/note.ts";
import { createPostgresConnection } from "https://deno.land/x/remult/postgres.ts";
import settings from "../../../../../../settings_nk.js";

/* configuration sammy */
export const remultServer = remultFresh({
  entities: [Note],
  dataProvider: async () => {
    return createPostgresConnection({
      configuration: {
        user: settings.dbsettings.user,
        password: settings.dbsettings.password,
        database: settings.dbsettings.database,
        hostname: settings.dbsettings.hostname,
        port: settings.dbsettings.port,
        tls: { enabled: false },
      },
    });
    return await undefined;
  },
}, Response);
export const handler = remultServer.handle;

