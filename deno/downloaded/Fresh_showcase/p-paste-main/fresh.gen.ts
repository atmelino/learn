// DO NOT EDIT. This file is generated by fresh.
// This file SHOULD be checked into source version control.
// This file is automatically updated during development when running `dev.ts`.

import config from "./deno.json" assert { type: "json" };
import * as $0 from "./routes/[id].tsx";
import * as $1 from "./routes/api/create.ts";
import * as $2 from "./routes/api/joke.ts";
import * as $3 from "./routes/index.tsx";
import * as $4 from "./routes/prism.css.ts";
import * as $$0 from "./islands/Back.tsx";
import * as $$1 from "./islands/Home.tsx";
import * as $$2 from "./islands/View.tsx";

const manifest = {
  routes: {
    "./routes/[id].tsx": $0,
    "./routes/api/create.ts": $1,
    "./routes/api/joke.ts": $2,
    "./routes/index.tsx": $3,
    "./routes/prism.css.ts": $4,
  },
  islands: {
    "./islands/Back.tsx": $$0,
    "./islands/Home.tsx": $$1,
    "./islands/View.tsx": $$2,
  },
  baseUrl: import.meta.url,
  config,
};

export default manifest;