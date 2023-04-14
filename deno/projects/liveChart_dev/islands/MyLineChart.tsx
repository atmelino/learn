import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";
import MyData from "./data.tsx";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import PeriodicTask from "./PeriodicTask.tsx";

export default function MyLineChart() {
  let timems = useRef(Date.now());
  let datasets1 = useRef(MyData());
  let update = useRef(false);
  // let value = useRef(30000);
  const [count, setCount] = useState(4);

  const [timestamp, settimestamp] = useState("");
  const [datasets, setData] = useState(datasets1.current);
  const [updateState, setUpdate] = useState(false);
  const [valueState, setValue] = useState(30000);
  const data1: { x: Date; y: number }[] = [];
  // let value = 30000;


  const getBtcData = async () => {
    fetch('https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD')
      .then(response => response.json())
      .then(data => {
        // console.log(data);
        setValue(data.USD);
        console.log(valueState);
      });
  }

  function addData() {
    // console.log("addData called");
    timems.current = Date.now();
    settimestamp(format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss"));
    getBtcData();
    if (datasets1.current[0].data.length >= 30) {
      datasets1.current[0].data.splice(0, 1);
    }
    datasets1.current[0].data.push({
      x: timems.current,
      y: valueState,
    });
    setData(datasets1.current);
    update.current = !update.current;
    setUpdate(update.current);
    // printData(datasets1.current);
  }

  function printtimems() {
    // console.log("timems " + JSON.stringify(timems, null, 4));
    const timestamp = format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss");
    // console.log("timems " + timestamp);
  }

  function printData(
    ds: { label: string; color: string; data: { x: number; y: number }[] }[],
  ) {
    console.log("length=" + ds[0].data.length);

    for (const d of ds[0].data) {
      const timestamp = format(new Date(d.x), "yyyy-MM-dd HH:mm:ss");
      console.log("x= " + timestamp + " y=" + d.y);
    }
  }

  return (
    <div>
      <Button onClick={() => { setCount(count - 1); console.log(count); }}>-1</Button>
      <Button onClick={() => { setValue(count - 1); console.log(count); }}>-1</Button>

      <div class="bg-green-100">
        <Button onClick={addData}>time step</Button>
        <PeriodicTask
          Task={addData}
          interval={1000} />
      </div>
      <b>{timestamp} 1 BTC = {valueState} USD</b>
      <LineChartDateMod
        height={400}
        datasets={datasets}
        data={data1}
        yAxisMin={30000}
        yAxisMax={31000}
        requestUpdate={updateState}
      >
      </LineChartDateMod>
    </div>
  );
}
