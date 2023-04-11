import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";
import MyData from "./data.tsx";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";

export default function MyLineChart() {
  // let datasets1=MyData();
  // const [timems, settimems] = useState(Date.now());
  let count = useRef(0);
  let timems = useRef(Date.now());
  let datasets1 = useRef(MyData());
  const [datasets, setData] = useState(datasets1.current);
  const [update, setUpdate] = useState(false);

  useEffect(() => {
    count.current = count.current + 1;
  });

  const data1: { x: Date; y: number }[] = [];

  function addData() {
    console.log("addData called");
    // printData(datasets1.current);

    timems.current = timems.current + 50000;
    // console.log("timems " + JSON.stringify(timems, null, 4));
    const timestamp = format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss");
    // console.log("timems " + timestamp);

    const value = Math.floor((Math.random() * 10) + 1);
    datasets1.current[0].data.splice(0, 1);
    // console.log(datasets1[0].data);
    datasets1.current[0].data.push({
      x: timems.current,
      y: value,
    });
    // console.log("datasets1 " + JSON.stringify(datasets1.current, null, 4));

    printData(datasets1.current);

    setData(datasets1.current);

    setUpdate(!update);

    // console.log("datasets " + JSON.stringify(datasets, null, 4));
  }

  function printData(
    ds: { label: string; color: string; data: { x: number; y: number }[] }[],
  ) {
    for (const d of ds[0].data) {
      const timestamp = format(new Date(d.x), "yyyy-MM-dd HH:mm:ss");

      console.log("x= " + timestamp+" y="+d.y);
    }

    // console.log("ds " + JSON.stringify(ds, null, 4));
    // console.log("ds " + ds[0].data[0].x);
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
