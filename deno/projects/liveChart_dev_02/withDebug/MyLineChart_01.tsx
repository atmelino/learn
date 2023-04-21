import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDynamic } from "../library/charts.ts";
import MyData from "./data.tsx";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import PeriodicTask from "./PeriodicTask.tsx";

export default function MyLineChart() {
  const timems = useRef(Date.now());
  const datasets1 = useRef(MyData());
  const update = useRef(false);
  const yAxisAuto = useRef(true);
  // const start = useRef("start");
  const [start, setstart] = useState("start");
  const [min, setMin] = useState(30000);
  const [max, setMax] = useState(31000);
  const [datasets, setData] = useState(datasets1.current);
  const [timestamp, settimestamp] = useState("");
  const [valueState, setValue] = useState();
  const [updateState, setUpdate] = useState(false);
  const renderCount = useRef(0);
  const noteRef = useRef<HTMLInputElement | null>(null);
  const [inputValue, setInputValue] = useState("");

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
    yAxisAuto.current = !yAxisAuto.current;
  };

  useEffect(() => {
  }, []);


  useEffect(() => {
    renderCount.current = renderCount.current + 1;
  });

  return (
    <>
      <h1>Render Count: {renderCount.current}</h1>

      <div class="p-4 mx-auto max-w-screen-md">
        <h2 class="text-lg font-medium text-gray-900 ">Live Bitcoin Chart</h2>
      </div>
      <div class="p-4 mx-auto max-w-screen-md">
        <form
          class="flex gap-2 w-full"
          onSubmit={(e) => {
            e.preventDefault();
            if (!noteRef?.current?.value) {
              return;
            }
            setInputValue(noteRef?.current?.value ?? "");
            // noteRef.current.value = "";
          }}
        >
          <input
            class="w-5/6 border-1 border-gray-500 h-10 rounded p-2"
            type="text"
            ref={noteRef}
          />
          <Button
            type="submit"
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-1/2"
          >
            Set
          </Button>
        </form>

        <div class="bg-green-100">
          <Button onClick={() => {
            console.log("start pressed");
            setstart("start");
            // start.current = "start"
            // console.log("start=" + start.current);

          }}>Start</Button>
          <Button onClick={() => {
            setstart("---");
          }}>---</Button>
          <Button onClick={() => {
            setstart("stop");
            // start.current = "stop"
          }}>Stop</Button>
          {"" + start}
          <label>
            y-axis: auto <input type="checkbox" checked={yAxisAuto.current} onChange={handleChange} />
          </label>
          <label>
            min
            <input disabled={yAxisAuto.current} type="number"
              placeholder="34"
              // value={min}
              id="min" name="tentacles"
              min="0" max="100000"></input>
            max
            <input disabled={yAxisAuto.current} type="number" value={max} id="max" name="tentacles"
              min="0" max="100000"></input>
          </label>
          <Button>Set</Button>

          <PeriodicTask
            Task={addData}
            name={"live BTC"}
            interval={1000}
            start={start}
          />
        </div>
        <LineChartDynamic
          height={500}
          datasets={datasets}
          data={data1}
          yAxisMin={min}
          yAxisMax={max}
          yAxisAuto={yAxisAuto.current}
          addLabel={false}
          addLegend={false}
        // requestUpdate={updateState}
        >
        </LineChartDynamic>
      </div>
      <div class="p-4 mx-auto max-w-screen-md">
        {timestamp} <b>1 BTC = {valueState} USD</b>
      </div>
    </>
  );
}
