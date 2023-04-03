import React, { useEffect, useRef, useState } from "react";
import PeriodicTask from "./components/PeriodicTask";
import PeriodicTask2 from "./components/PeriodicTask2";

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

export const options1 = {
  showLines: true,
  animation: { duration: 0 },
  scales: {
    yAxes: [{
      display: true,
      ticks: {
        beginAtZero: true,
        min: 0,
        max: 100,
      },
    }],
  },
  maintainAspectRatio: false,
};

export const options = {
  showLines: true,
  animation: { duration: 0 },

  scales: {
    y: {
      beginAtZero: true,
    },
  },
};

export const data = {
  labels: [1, 2, 3, 4, 5, 6],

  datasets: [
    {
      label: "My First dataset",
      fill: false,
      lineTension: 0.0,
      backgroundColor: "rgba(75,192,192,0.4)",
      borderColor: "rgba(75,192,192,1)",
      borderCapStyle: "butt",
      borderDash: [],
      borderDashOffset: 0.0,
      borderJoinStyle: "miter",
      pointBorderColor: "rgba(75,192,192,1)",
      pointBackgroundColor: "#fff",
      pointBorderWidth: 1,
      pointHoverRadius: 5,
      pointHoverBackgroundColor: "rgba(75,192,192,1)",
      pointHoverBorderColor: "rgba(220,220,220,1)",
      pointHoverBorderWidth: 2,
      pointRadius: 5,
      pointHitRadius: 10,
      data: [65, 59, 80, 0, 56, 55, 40],
    },
  ],
};

var zero = 7;

type ButtonProps = {
  onClick(): void;
  name: string;
  children: React.ReactNode;
};

export default function App() {
  const [count, setCount] = useState(0);

  function handleClick() {
    console.log("Function ran in Child component");
    setCount(count + 1);
  }

  useEffect(() => {
    document.title = "example_05";
  }, []);

  const chartRef = useRef<ChartJS>(null);

  function addData() {
    console.log("addData called");
    const { current: chart } = chartRef;
    if (!chart) {
      return;
    }

    var value = Math.floor((Math.random() * 100) + 1);
    data.labels.push(zero);
    data.labels.splice(0, 1);
    data.datasets[0].data.splice(0, 1);
    console.log(data.datasets[0].data);
    data.datasets[0].data.push(value);

    chart.update();
    zero++;
    return;
  }

  return (
    <div>
      <div>
        <PeriodicTask2 name="James" onClick={addData}>
          <span>Click me</span>
        </PeriodicTask2>
      </div>

      <button onClick={() => addData()}>Add Data</button>

      <Chart
        // width={"5%"}
        height={"50%"}
        ref={chartRef}
        type="line"
        options={options}
        data={data}
      />
    </div>
  );
}
