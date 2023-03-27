// App.js
import Chart from "chart.js/auto";
import { CategoryScale } from "chart.js";
import { useState } from "react";
import { Data } from "../utils/Data";
import PieChart from "./components/PieChart";
import "./styles.css";

Chart.register(CategoryScale);

export default function App() {
  const [chartData, setChartData] = useState({
    // ...chart data
  });
 
  return (
    <div className="App">
      <PieChart chartData={chartData} />
    </div>
  );
}