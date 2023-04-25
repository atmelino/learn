import { useEffect, useRef, useState } from "preact/hooks";
import { LineChartDynamic } from "https://raw.githubusercontent.com/atmelino/d3no-data/livechart/charts.ts"
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";

export default function MyLineChart() {
  const timems = useRef(Date.now());
  const datasets1 = useRef([
    {
      label: "data",
      color: "green",
      data: [
      ],
    },
  ]);
  const [datasets, setData] = useState(datasets1.current);
  const [timestamp, settimestamp] = useState("0000-00-00 00:00:00");

  // used for example purposes
  function getRandomIntInclusive(min: number, max: number) {
    min = Math.ceil(min);
    max = Math.floor(max);
    return Math.floor(Math.random() * (max - min + 1)) + min;
  }

  function addData() {
    // console.log("addData called");
    timems.current = Date.now();
    settimestamp(format(new Date(timems.current), "yyyy-MM-dd HH:mm:ss"));

    const value = getRandomIntInclusive(1, 25)
    if (datasets1.current[0].data.length >= 30) {
      datasets1.current[0].data.splice(0, 1);
    }
    datasets1.current[0].data.push({
      x: timems.current,
      y: value,
    });

    setData(datasets1.current);
  }

  useEffect(() => {
    // get new data every x seconds
    setInterval(addData, 1000);
  }, []);

  return (
    <>
      <div class="flex flex-row justify-evenly">
        <label class="w-11/12 flex justify-center  text-lg font-medium text-gray-900 ">
          D3NO DATA Live Chart
        </label>
      </div>

      <div class="flex flex-row justify-evenly bg-green-50">
        <LineChartDynamic
          addTitle={true}
          height={500}
          paddingTop={10}
          datasets={datasets}
          data={datasets[0].data}
          yAxisAuto={true}
          addLabel={false}
          addLegend={false}
          addTooltip={false}
        >
        </LineChartDynamic>
      </div>
    </>
  );
}
