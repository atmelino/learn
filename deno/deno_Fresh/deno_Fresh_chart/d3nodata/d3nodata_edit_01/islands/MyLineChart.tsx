import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDynamic } from "../library/charts.ts";
import MyData from "./data.tsx";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";

export default function MyLineChart() {
  // let datasets1=MyData();
  // const [timems, settimems] = useState(Date.now());
  let timems = useRef(Date.now());
  let datasets1 = useRef(MyData());
  const [datasets, setData] = useState(datasets1.current);
  const [update, setUpdate] = useState(false);
  const data1: { x: Date; y: number }[] = [];

  function addData() {
    timems.current = timems.current + 50000;
    const value = Math.floor((Math.random() * 10) + 1);
    if (datasets1.current[0].data.length > 20) {
      datasets1.current[0].data.splice(0, 1);
    }
    datasets1.current[0].data.push({
      x: timems.current,
      y: value,
    });
    setData(datasets1.current);
    setUpdate(!update);
  }

  function printtimems() {
    // console.log("timems " + JSON.stringify(timems, null, 4));
    const timestamp = format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss");
    // console.log("timems " + timestamp);
  }

  function printData(
    ds: { label: string; color: string; data: { x: number; y: number }[] }[],
  ) {
    for (const d of ds[0].data) {
      const timestamp = format(new Date(d.x), "yyyy-MM-dd HH:mm:ss");

      console.log("x= " + timestamp + " y=" + d.y);
    }
  }

  return (
    <div>
      <div>
        <Button onClick={addData}>time step</Button>

        {/* {JSON.stringify(datasets, null, 4)} */}
        {/* {test} */}
      </div>
      <LineChartDynamic
        datasets={datasets}
        data={data1}
        yAxisMax={10}
        yAxisMin={0}
        requestUpdate={update}
      >
      </LineChartDynamic>    </div>
  );
}
