import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDynamic } from "../library/charts.ts";
import MyData from "./data.tsx";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import PeriodicTask from "./PeriodicTask.tsx";
import Popup from "./Popup.tsx";

export default function MyLineChart() {
  const timems = useRef(Date.now());
  const datasets1 = useRef(MyData());
  const yAxisAuto = useRef(true);
  // const [yAxisAuto, setyAxisAuto] = useState(true);
  const [start, setstart] = useState("start");
  const [min, setMin] = useState(0);
  const [max, setMax] = useState(100000);
  const [datasets, setData] = useState(datasets1.current);
  const [timestamp, settimestamp] = useState("");
  const [valueState, setValue] = useState();
  const renderCount = useRef(0);
  const data1: { x: Date; y: number }[] = [];
  let value = 30000;

  const getBtcData = () => {
    fetch("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD")
      .then(response => response.json())
      .then(data => {
        // console.log(data);
        value = data.USD;
        setValue(data.USD);
        if (datasets1.current[0].data.length >= 30) {
          datasets1.current[0].data.splice(0, 1);
        }
        datasets1.current[0].data.push({
          x: timems.current,
          y: value,
        });
        setData(datasets1.current);
        // printData(datasets1.current);
      })
      .catch(() => {
        console.log('Data failed to load from url');
      });
  }


  function addData() {
    // console.log("addData called");
    timems.current = Date.now();
    settimestamp(format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss"));
    getBtcData();
    // console.log(yAxisAuto);
    // console.log("showDebug=" + showDebug);
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

  function setyAxisAutoRef(val: boolean) {
    yAxisAuto.current = val;
  }

  useEffect(() => {
    renderCount.current = renderCount.current + 1;
  });

  return (
    <>

      <Popup
        title="Settings"
        // yAxisAuto={yAxisAuto}
        setyAxisAutoRef={setyAxisAutoRef}
        min={min}
        setMin={setMin}
        max={max}
        setMax={setMax}
      />

      <div class="mx-auto max-w-screen-md">
        <h2 class="text-lg font-medium text-gray-900 ">Live Bitcoin Chart</h2>
      </div>
      <div class="mx-auto max-w-screen-md">

        <div class="bg-green-100">
          <Button onClick={() => {
            console.log("start pressed");
            setstart("start");
            // setyAxisAuto(false);
            // console.log(yAxisAuto);

            // start.current = "start"
            // console.log("start=" + start.current);

          }}>Start</Button>
          <Button onClick={() => {
            setstart("stop");
            // start.current = "stop"
          }}>Stop</Button>
          {"    " + start}

          <PeriodicTask
            Task={addData}
            name={"live BTC"}
            interval={1000}
            start={start}
          />
        </div>
        <div class="mx-auto max-w-screen-md">
          {timestamp} <b>1 BTC = {valueState} USD</b>
        </div>
        <LineChartDynamic
          height={500}
          paddingTop={10}
          datasets={datasets}
          data={data1}
          yAxisMin={min}
          yAxisMax={max}
          yAxisAuto={yAxisAuto.current}
          addLabel={false}
          addLegend={false}
          addTooltip={false}
        >
        </LineChartDynamic>
      </div>
    </>
  );
}
