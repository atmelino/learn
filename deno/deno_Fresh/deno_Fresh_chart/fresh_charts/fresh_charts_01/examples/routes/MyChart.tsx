import { useState } from "preact/hooks";
import { Chart } from "$fresh_charts/mod.ts";
import { months, numbers } from "../utils.ts";
import { ChartColors, transparentize } from "$fresh_charts/utils.ts";

export default function MyChart() {
  const barCfg = { count: 7, min: -100, max: 100 };
  const [mynumbers, setmynumbers] = useState(numbers(barCfg));

  const addNote = () => {
    console.log("addNote called");
    setmynumbers(numbers(barCfg));
  };

  return (
    <div class="p-4 mx-auto max-w-screen-md">
      <h1 class="text(xl gray-600) font-medium mt-4">Bar Chart - Inline</h1>
      <Chart
        type="bar"
        options={{ devicePixelRatio: 1 }}
        data={{
          labels: months(barCfg),
          datasets: [
            {
              label: "Dataset 1",
              data: mynumbers,
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
  );
}
