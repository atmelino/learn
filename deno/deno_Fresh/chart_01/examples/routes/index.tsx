// Copyright 2018-2022 the Deno authors. All rights reserved. MIT license.

import { Head } from "$fresh/runtime.ts";
import { Chart } from "$fresh_charts/mod.ts";
import { ChartColors, transparentize } from "$fresh_charts/utils.ts";
import { months, numbers } from "../utils.ts";
import MyChart from "../islands/MyChart.tsx";

export default function Home() {
  const barCfg = { count: 7, min: -100, max: 100 };
  return (
    <div>
      <Head>
        <title>Fresh Charts Examples</title>
      </Head>

      <div class="p-4 mx-auto max-w-screen-md">
        <MyChart />
      </div>
    </div>
  );
}
