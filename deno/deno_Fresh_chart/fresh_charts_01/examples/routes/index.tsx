import { Head } from "$fresh/runtime.ts";
import { Chart } from "$fresh_charts/mod.ts";
import { ChartColors, transparentize } from "$fresh_charts/utils.ts";
import { months, numbers } from "../utils.ts";
import MyChart from "./MyChart.tsx";
import MyIsland from "../islands/MyIsland.tsx";

export default function Home() {
  const barCfg = { count: 7, min: -100, max: 100 };
  return (
    <div>
      <Head>
        <title>Fresh Charts Examples</title>
      </Head>

      <div>
        <MyIsland />
      </div>

      <div class="p-4 mx-auto max-w-screen-md">
        <MyChart />
      </div>
    </div>
  );
}
