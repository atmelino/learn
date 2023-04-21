import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDynamic } from "../library/charts.ts";
import MyData from "./data.tsx";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import PeriodicTask from "./PeriodicTask.tsx";
import { ButtonGreen } from "../components/ButtonGreen.tsx";

export default function MyLineChart() {
  const timems = useRef(Date.now());
  const datasets1 = useRef(MyData());
  const update = useRef(false);
  const yAxisAuto = useRef(true);
  const [start, setstart] = useState("start");
  const [min, setMin] = useState(0);
  const [max, setMax] = useState(100000);
  const [datasets, setData] = useState(datasets1.current);
  const [timestamp, settimestamp] = useState("");
  const [valueState, setValue] = useState();
  const renderCount = useRef(0);
  const minRef = useRef<HTMLInputElement | null>(null);
  const maxRef = useRef<HTMLInputElement | null>(null);
  const [field, setField] = useState("border border-solid border-gray-300 p-3 space-x-3");
  const [disabled, setDisabled] = useState(" text-gray-300");


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
        update.current = !update.current;
        // console.log("update="+update.current)
        // setUpdate(update.current);
        // printData(datasets1.current);
      })
      .catch(() => {
        console.log('Data failed to load from url');
      });
  }


  function addData() {
    console.log("addData called");
    timems.current = Date.now();
    settimestamp(format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss"));
    getBtcData();
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

  const handleChange = () => {
    console.log("handleChange called")
    yAxisAuto.current = !yAxisAuto.current;
    // setField("border border-solid border-red-300 p-3 space-x-3 text-gray-300");
    // if(yAxisAuto.current)
    setDisabled(yAxisAuto.current ? "text-black" : " text-gray-300");
  };

  useEffect(() => {
    renderCount.current = renderCount.current + 1;
  });

  function clickSet() {
    if (minRef?.current?.value)
      setMin(+minRef?.current?.value);
    if (maxRef?.current?.value)
      setMax(+maxRef?.current?.value);
  }


  return (
    <>
      {/* <h1>Render Count: {renderCount.current}</h1> */}

      <div class="mx-auto max-w-screen-md">
        <h2 class="text-lg font-medium text-gray-900 ">Live Bitcoin Chart</h2>
      </div>
      <div class="mx-auto max-w-screen-md">

        <fieldset class="border border-solid border-gray-300 p-2 rounded space-x-3"
          disabled={yAxisAuto.current}
        >
          <legend class="text-sm space-x-3">
            y-Axis Scale<label>   </label><input type="checkbox" checked={yAxisAuto.current} onChange={handleChange} />
            <label class={disabled}>auto</label>
          </legend>
          <div class={yAxisAuto.current ? " text-gray-300" : "text-black"} disabled={yAxisAuto.current}>
            <label>  Min  </label>
            <input
              class={"w-1/6 border-1 border-gray-500 h-8 rounded p-2"}
              disabled={yAxisAuto.current}
              type="number"
              id="min"
              min="0" max="100000"
              ref={minRef}
            />
            <label>   Max  </label>
            <input
              class="w-1/6 border-1 border-gray-500 h-8 rounded p-2"
              disabled={yAxisAuto.current}
              type="number"
              id="max"
              min="0" max="100000"
              ref={maxRef}
            />
            <label>     </label>
            <Button
             class={yAxisAuto.current ? "text-gray-300" : "text-black"} disabled={yAxisAuto.current}
              onClick={clickSet}
            >Set
            </Button>
          </div>
        </fieldset>


        <div class="bg-green-100">
          <Button onClick={() => {
            console.log("start pressed");
            setstart("start");
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
      <div class="mx-auto max-w-screen-md">
        {timestamp} <b>1 BTC = {valueState} USD</b>
      </div>
    </>
  );
}
