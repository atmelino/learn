// Copyright 2018-2022 the Deno authors. All rights reserved. MIT license.

import { Head } from "$fresh/runtime.ts";
import { Chart } from "$fresh_charts/mod.ts";
import { ChartColors, transparentize } from "$fresh_charts/utils.ts";
import { months, numbers } from "../utils.ts";
import Counter from "../islands/Counter.tsx";
import MyIsland from "../islands/MyIsland.tsx";

export default function Home() {
  const barCfg = { count: 7, min: -100, max: 100 };
  const [mynumbers, setmynumbers] = useState(numbers(barCfg));
  return (
    <>
      <Head>
        <title>Fresh Charts Examples</title>
      </Head>
      <div class="p-4 mx-auto max-w-screen-md">
        <div class="flex items-center">
          <img
            src="/logo.svg"
            class="w-32 h-32"
            alt="the fresh logo: a sliced lemon dripping with juice"
          />
          <div>
            <h1 class="text(4xl gray-700) font-bold">Fresh Charts</h1>
            <h2 class="text(xl gray-600) font-medium">Examples</h2>
          </div>
        </div>
        <div>
          <Counter start={3} />
        </div>
        <div>
        <MyIsland/>
        </div>
        <h1 class="text(xl gray-600) font-medium mt-4">Bar Chart - Inline</h1>
        <Chart
          type="bar"
          options={{ devicePixelRatio: 1 }}
          data={{
            labels: months(barCfg),
            datasets: [
              {
                label: "Dataset 1",
                data: numbers(barCfg),
                backgroundColor: ChartColors.Red,
              },
              {
                label: "Dataset 2",
                data: numbers(barCfg),
                backgroundColor: ChartColors.Blue,
              },
              {
                label: "Dataset 3",
                data: numbers(barCfg),
                backgroundColor: ChartColors.Green,
              },
            ],
          }}
        />
      </div>
    </>
  );
}

function useState(arg0: (number|null)[]): [any,any] {
throw new Error("Function not implemented.");
}
