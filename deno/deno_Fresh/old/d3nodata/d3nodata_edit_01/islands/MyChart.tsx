import { useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { BarChart } from "../library/charts.ts";

export default function MyChart() {
  const datasets1 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          y: 2,
          x: "x1",
        },
        {
          y: 3,
          x: "x2",
        },
        {
          y: 5,
          x: "x3",
        },
      ],
    },
  ];

  const data1 = [
    {
      y: 2,
      x: "x1",
    },
    {
      y: 5,
      x: "x2",
    },
    {
      y: 1,
      x: "x3",
    },
  ];

  const [datasets, setData] = useState(datasets1);
  const [test, setTest] = useState("initial");

  let titleOnOff = true;

  const changeData = () => {
    console.log("changeData called");

    console.log("datasets before" + JSON.stringify(datasets, null, 4));
    datasets1[0].data[0] = {
      y: 8,
      x: "x1",
    };
    setData(datasets1);
    console.log("datasets after" + JSON.stringify(datasets, null, 4));
    setTest("changed");
    titleOnOff = false;
  };

  return (
    <div>
      <div>
        <Button onClick={changeData}>change Data</Button>
        {JSON.stringify(datasets, null, 4)}
        {test}
      </div>
      <BarChart
        datasets={datasets}
        data={data1}
        addTitle={titleOnOff}
        passedDown={test}
      >
      </BarChart>
    </div>
  );
}
