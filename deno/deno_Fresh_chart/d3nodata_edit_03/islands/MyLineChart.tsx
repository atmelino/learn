import { useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";

export default function MyLineChart() {
  const datasets1 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          x: new Date(10000000000),
          y: 2,
        },
        {
          x: new Date(20000000000),
          y: 4,
        },
        {
          x: new Date(30000000000),
          y: 3,
        },
      ],
    },
  ];
  const data1: { x: Date; y: number }[] = [];

  const [datasets, setData] = useState(datasets1);
  const [test, setTest] = useState("initial");

  let titleOnOff = true;

  const changeData = () => {
    console.log("changeData called");
    // console.log("datasets before" + JSON.stringify(datasets, null, 4));
    datasets1[0].data[0] = {
      x: new Date(10000000000),
      y: 8,
    };
    datasets1[0].data.push({
      x: new Date(40000000000),
      y: 2,
    });
    setData(datasets1);
    // console.log("datasets after" + JSON.stringify(datasets, null, 4));
    setTest("changed");
    titleOnOff = false;
  };

  return (
    <div>
      <div>
        <Button onClick={changeData}>change Data</Button>
        {JSON.stringify(datasets, null, 4)}
        {/* {test} */}
      </div>
      <LineChartDateMod
        datasets={datasets}
        data={data1}
        addTitle={titleOnOff}
        passedDown={test}
      >
      </LineChartDateMod>
    </div>
  );
}
