import { useState } from "preact/hooks";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import { Button } from "../components/Button.tsx";
import { Chart } from "$fresh_charts/mod.ts";
import { months, numbers } from "../utils.ts";
import { ChartColors, transparentize } from "$fresh_charts/utils.ts";

export default function MyChart() {
  const barCfg = { count: 7, min: -100, max: 100 };
  const pieCfg = { count: 5, min: 0, max: 100 };


  const addNote = () => {
    console.log("addNote called");
  };

  return (
    <>
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
        <Button onClick={addNote}>Add Note</Button>
      </div>
    </>
  );
}
