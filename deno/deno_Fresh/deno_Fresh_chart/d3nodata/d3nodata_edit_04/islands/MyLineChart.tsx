import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";
import MyData from "./data.tsx";

export default function MyLineChart() {
  const [datasets, setData] = useState(MyData());
  const [update, setUpdate] = useState("initial");
  // const [timems, settimems] = useState(Date.now());
  let count = useRef(0);
  let timems = useRef(Date.now());

  useEffect(() => {
    count.current = count.current + 1;
  });

  const data1: { x: Date; y: number }[] = [];

  function addData() {
    console.log("addData called");

    // settimems(timems + 100000);
    // count = count + 10000;
    // settimems(2);
    timems.current = timems.current + 10000;
    // console.log("timems " + timems);
    console.log("timems " + JSON.stringify(timems, null, 4));
    count.current = count.current + 1;

    // const value = Math.floor((Math.random() * 10) + 1);
    // datasets1[0].data.splice(0, 1);
    // console.log(datasets1[0].data);
    // datasets[0].data.push({
    //   x: new Date(timems + 30000),
    //   y: value,
    // });
    // console.log("datasets1 " + JSON.stringify(datasets1, null, 4));

    // setData(datasets);

    setUpdate("changed");

    // console.log("datasets " + JSON.stringify(datasets, null, 4));
  }

  const changeData = () => {
    console.log("changeData called");

    // settimems(timems + 100000);
    // datasets1[0].data.push({
    //   x: new Date(timems + 30000),
    //   y: 2,
    // });
    // setData(datasets1);
    // console.log("datasets after" + JSON.stringify(datasets, null, 4));
    setUpdate("changed");
  };

  return (
    <div>
      <div>
        <Button onClick={changeData}>change Data</Button>
        <Button onClick={addData}>time step</Button>
        <h1>Render Count: {count.current}</h1>

        {/* {JSON.stringify(datasets, null, 4)} */}
        {/* {test} */}
      </div>
      <LineChartDateMod
        datasets={datasets}
        data={data1}
        requestUpdate={update}
      >
      </LineChartDateMod>
    </div>
  );
}

// let datasets2 = [
//   {
//     label: "test",
//     color: "green",
//     data: [
//       {
//         x: new Date(10000),
//         y: 2,
//       },
//       {
//         x: new Date(20000),
//         y: 4,
//       },
//       {
//         x: new Date(30000),
//         y: 3,
//       },
//     ],
//   },
// ];

// let datasets1 = [
//   {
//     label: "test",
//     color: "green",
//     data: [
//       {
//         x: new Date(Date.now()),
//         y: 2,
//       },
//       {
//         x: new Date(Date.now() + 10000),
//         y: 4,
//       },
//       {
//         x: new Date(Date.now() + 20000),
//         y: 3,
//       },
//     ],
//   },
// ];
