import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";
import MyData from "./data.tsx";

export default function MyLineChart() {
  // let datasets1=MyData();
  // const [timems, settimems] = useState(Date.now());
  let count = useRef(0);
  let timems = useRef(Date.now());
  let datasets1 = useRef(MyData());
  const [datasets, setData] = useState(datasets1.current);
  const [update, setUpdate] = useState("initial");

  useEffect(() => {
    count.current = count.current + 1;
  });

  const data1: { x: Date; y: number }[] = [];

  function addData() {
    console.log("addData called");

    // settimems(timems + 100000);
    // settimems(2);
    timems.current = timems.current + 10000;
    // console.log("timems " + timems);
    console.log("timems " + JSON.stringify(timems, null, 4));
    const value = Math.floor((Math.random() * 10) + 1);
    // datasets1[0].data.splice(0, 1);
    // console.log(datasets1[0].data);
    datasets1.current[0].data.push({
      x: timems.current,
      y: value,
    });
    console.log("datasets1 " + JSON.stringify(datasets1.current, null, 4));

    setData(datasets1.current);

    setUpdate("changed");

    // console.log("datasets " + JSON.stringify(datasets, null, 4));
  }

  return (
    <div>
      <div>
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
