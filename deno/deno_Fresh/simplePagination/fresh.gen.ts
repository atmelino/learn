// DO NOT EDIT. This file is generated by fresh.
// This file SHOULD be checked into source version control.
// This file is automatically updated during development when running `dev.ts`.

import config from "./deno.json" assert { type: "json" };
import * as $0 from "./routes/index.tsx";
import * as $$0 from "./islands/Body.tsx";
import * as $$1 from "./islands/DataTable.tsx";
import * as $$2 from "./islands/myData.tsx";

const manifest = {
  routes: {
    "./routes/index.tsx": $0,
  },
  islands: {
    "./islands/Body.tsx": $$0,
    "./islands/DataTable.tsx": $$1,
    "./islands/myData.tsx": $$2,
  },
  baseUrl: import.meta.url,
  config,
};

export default manifest;