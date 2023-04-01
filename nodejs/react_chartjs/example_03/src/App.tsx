import { MouseEvent, useRef } from "react";
import type {
  BubbleDataPoint,
  ChartTypeRegistry,
  InteractionItem,
  Point,
} from "chart.js";
import React, { useEffect } from "react";

import {
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LinearScale,
  LineElement,
  PointElement,
  Tooltip,
} from "chart.js";
import {
  Chart,
  getDatasetAtEvent,
  getElementAtEvent,
  getElementsAtEvent,
} from "react-chartjs-2";

ChartJS.register(
  LinearScale,
  CategoryScale,
  BarElement,
  PointElement,
  LineElement,
  Legend,
  Tooltip,
);

export const options = {
  scales: {
    y: {
      beginAtZero: true,
    },
  },
};

const labels = ["January", "February", "March", "April", "May", "June", "July"];

export const data = {
  labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
  datasets: [
    {
      type: "line" as const,
      label: "Dataset 1",
      borderColor: "rgb(255, 99, 132)",
      //data: [12, 19, 3, 5, 2, 30],
      data: [12, 19],
      borderWidth: 2,
    },
    {
      type: "bar" as const,
      label: "Dataset 2",
      backgroundColor: "rgb(75, 192, 192)",
      data: [12, 19, 3, 5, 2, 3],
      borderColor: "white",
      borderWidth: 1,
    },
    // {
    //   type: "bar" as const,
    //   label: "Dataset 3",
    //   data: [12, 19, 3, 5, 2, 3],
    //   backgroundColor: "rgb(53, 162, 235)",
    // },
  ],
};

export default function App() {
  useEffect(() => {
    document.title = "example_03";
  }, []);

  const getInfo = (
    chart: ChartJS<
      keyof ChartTypeRegistry,
      (number | [number, number] | Point | BubbleDataPoint | null)[],
      unknown
    >,
    event: MouseEvent<HTMLCanvasElement, globalThis.MouseEvent>,
  ) => {
    const dataset = getDatasetAtEvent(chart, event);
    console.log("printDatasetAtEvent dataset.length=" + dataset.length);
    if (!dataset.length) return;
    const datasetIndex1 = dataset[0].datasetIndex;
    console.log(data.datasets[datasetIndex1].label);

    const element = getElementAtEvent(chart, event);
    console.log("printElementAtEvent element.length=" + element.length);
    if (!element.length) return;
    const { datasetIndex, index } = element[0];
    console.log(data.labels[index], data.datasets[datasetIndex].data[index]);

    const elements = getElementsAtEvent(chart, event);
    console.log("printElementsAtEvent elements.length=" + elements.length);
    if (!elements.length) return;
    console.log(elements.length);
  };

  const chartRef = useRef<ChartJS>(null);

  const onClick = (event: MouseEvent<HTMLCanvasElement>) => {
    const { current: chart } = chartRef;

    if (!chart) {
      return;
    }

    getInfo(chart, event);
  };

  function updateChart() {
    console.log("updateChart called");
    const { current: chart } = chartRef;

    if (!chart) {
      return;
    }

    console.log(JSON.stringify(data.datasets[0], null, 4));
    //data.datasets[0].data = [1, 2, 3, 4, 5, 3];
    data.datasets[0].data.push(29);
    console.log(JSON.stringify(data.datasets[0], null, 4));

    chart.update();
  }

  return (
    <div>
      <div>
        <button onClick={() => updateChart()}>Update Chart</button>
      </div>

      <Chart
        ref={chartRef}
        type="bar"
        onClick={onClick}
        options={options}
        data={data}
      />
    </div>
  );
}
