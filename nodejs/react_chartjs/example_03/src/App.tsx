import { MouseEvent, useRef } from "react";
import type { InteractionItem } from "chart.js";
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
      data: [12, 19, 3, 5, 2, 3],
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
    {
      type: "bar" as const,
      label: "Dataset 3",
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: "rgb(53, 162, 235)",
    },
  ],
};

export default function App() {
  useEffect(() => {
    document.title = "example_03";
  }, []);

  const printDatasetAtEvent = (dataset: InteractionItem[]) => {
    if (!dataset.length) return;

    const datasetIndex = dataset[0].datasetIndex;

    console.log(data.datasets[datasetIndex].label);
  };

  const printElementAtEvent = (element: InteractionItem[]) => {
    if (!element.length) return;

    const { datasetIndex, index } = element[0];

    console.log(data.labels[index], data.datasets[datasetIndex].data[index]);
  };

  const printElementsAtEvent = (elements: InteractionItem[]) => {
    if (!elements.length) return;

    console.log(elements.length);
  };

  const chartRef = useRef<ChartJS>(null);

  const onClick = (event: MouseEvent<HTMLCanvasElement>) => {
    const { current: chart } = chartRef;

    if (!chart) {
      return;
    }

    printDatasetAtEvent(getDatasetAtEvent(chart, event));
    printElementAtEvent(getElementAtEvent(chart, event));
    printElementsAtEvent(getElementsAtEvent(chart, event));
  };

  function updateChart() {
    console.log("updateChart called");
    const { current: chart } = chartRef;

    if (!chart) {
      return;
    }

    data.datasets[0].data=[1, 2, 3, 4, 5, 3];
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
