import { useState } from "react";
import { Data } from "./Data";
import { BarChart } from "./BarChart";
import LineChart from "./LineChart";
import PieChart from ".//PieChart";
import "./styles.css";
import { CategoryScale } from "chart.js";
import Chart from "chart.js/auto";

Chart.register(CategoryScale);

export default function App() {
  const [chartData, setChartData] = useState({
    labels: Data.map((data) => data.year),

    datasets: [
      {
        label: "Users Gained ",
        data: Data.map((data) => data.userGain),
        backgroundColor: [
          "rgba(75,192,192,1)",
          "#ecf0f1",
          "#f0331a",
          "#f3ba2f",
          "#2a71d0"
        ],
        borderColor: "black",
        borderWidth: 2
      }
    ]
  });

  return (
    <div className="App">
      <BarChart chartData={chartData} />
      <LineChart chartData={chartData} />
      <PieChart chartData={chartData} />
    </div>
  );
}


// // App.js
// import Chart from "chart.js/auto";
// import { CategoryScale } from "chart.js";
// import { useState } from "react";
// import { Data } from "./Data";
// import PieChart from "../components/PieChart";
// import "./styles.css";

// Chart.register(CategoryScale);

// export default function App() {
//   const [chartData, setChartData] = useState({
//     // ...chart data
//   });
 
//   return (
//     <div className="App">
//       <PieChart chartData={chartData} />
//     </div>
//   );

//   }




// // App.js
// import Chart from "chart.js/auto";
// import { CategoryScale } from "chart.js";
// import { useState } from "react";
// import { Data } from "./Data";
// import "./styles.css";

// Chart.register(CategoryScale);
 
// export default function App() {
//   const [chartData, setChartData] = useState({
//     labels: Data.map((data) => data.year), 
//     datasets: [
//       {
//         label: "Users Gained ",
//         data: Data.map((data) => data.userGain),
//         // backgroundColor: [
//         //   "rgba(75,192,192,1)",
//         //   &quot;#ecf0f1",
//         //   "#50AF95",
//         //   "#f3ba2f",
//         //   "#2a71d0"
//         // ],
//         borderColor: "black",
//         borderWidth: 2
//       }
//     ]
//   });
 
//   return (
//     <div className="App">
//       <p>Using Chart.js in React</p>
//     </div>
//   );
// }




// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;

