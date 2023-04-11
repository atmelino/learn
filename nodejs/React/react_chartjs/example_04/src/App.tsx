import React, { useEffect, useRef } from "react";
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
import { Chart } from "react-chartjs-2";

ChartJS.register(
  LinearScale,
  CategoryScale,
  BarElement,
  PointElement,
  LineElement,
  Legend,
  Tooltip,
);

export const data = {
  labels: ["January", "February", "March", "April", "May", "June", "July"],
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
    {
      type: "bar" as const,
      label: "Dataset 3",
      data: [12, 19, 3, 5, 2, 3],
      backgroundColor: "rgb(53, 162, 235)",
    },
  ],
};

function triggerTooltip(chart: ChartJS | null) {
  const tooltip = chart?.tooltip;

  if (!tooltip) {
    return;
  }

  if (tooltip.getActiveElements().length > 0) {
    tooltip.setActiveElements([], { x: 0, y: 0 });
  } else {
    const { chartArea } = chart;

    tooltip.setActiveElements(
      [
        {
          datasetIndex: 1,
          index: 2,
        },
        {
          datasetIndex: 1,
          index: 2,
        },
      ],
      {
        x: (chartArea.left + chartArea.right) / 2,
        y: (chartArea.top + chartArea.bottom) / 2,
      },
    );
  }

  chart.update();
}

export default function App() {
  useEffect(() => {
    document.title = "example_04";
  }, []);

  const chartRef = useRef<ChartJS>(null);

  useEffect(() => {
    const chart = chartRef.current;

    triggerTooltip(chart);
  }, []);


  function updateChart() {
    console.log("updateChart called");
    const { current: chart } = chartRef;

    if (!chart) {
      return;
    }

    console.log(JSON.stringify(data.datasets[0], null, 4));
    //data.datasets[0].data = [1, 2, 3, 4, 5, 3];
    data.datasets[0].data.push(29);
    data.labels.push("August");
    console.log(JSON.stringify(data.datasets[0], null, 4));

    chart.update();
  }

  return (
    <div>
      <button onClick={() => updateChart()}>Update Chart</button>

      <Chart ref={chartRef} type="bar" data={data} />
    </div>
  );
}
