import { useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";

export default function MyLineChart() {
  let timems = Date.now();
  const datasets1 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          x: new Date(timems),
          y: 2,
        },
        {
          x: new Date(timems + 1000),
          y: 4,
        },
        {
          x: new Date(timems + 2000),
          y: 3,
        },
        {
          x: new Date(timems + 3000),
          y: 1,
        },
      ],
    },
  ];
  const data1: { x: Date; y: number }[] = [];

  const [datasets, setData] = useState(datasets1);
  const [update, setUpdate] = useState("initial");

  let titleOnOff = true;

  function addData() {
    console.log("addData called");

    timems += 1000;
    const value = Math.floor((Math.random() * 100) + 1);
    datasets1[0].data.splice(0, 1);
    // console.log(datasets1[0].data);
    console.log("datasets " + JSON.stringify(datasets, null, 4));
    datasets1[0].data.push({
      x: new Date(timems + 3000),
      y: value,
    });
    setData(datasets1);
    setUpdate("changed");
  }

  const changeData = () => {
    console.log("changeData called");
    // console.log("datasets before" + JSON.stringify(datasets, null, 4));
    // datasets1[0].data[0] = {
    //   x: new Date(timems),
    //   y: 8,
    // };

    timems += 1000;
    datasets1[0].data.push({
      x: new Date(timems + 3000),
      y: 2,
    });
    setData(datasets1);
    // console.log("datasets after" + JSON.stringify(datasets, null, 4));
    setUpdate("changed");
    titleOnOff = false;
  };

  return (
    <div>
      <div>
        <Button onClick={changeData}>change Data</Button>
        <Button onClick={addData}>time step</Button>
        {/* {JSON.stringify(datasets, null, 4)} */}
        {/* {test} */}
      </div>
      <LineChartDateMod
        datasets={datasets}
        data={data1}
        addTitle={titleOnOff}
        requestUpdate={update}
      >
      </LineChartDateMod>
    </div>
  );
}
