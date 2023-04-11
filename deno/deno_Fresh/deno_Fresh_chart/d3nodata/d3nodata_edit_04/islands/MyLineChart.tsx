import { useState, useRef  } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";

export default function MyLineChart() {
  let datasets2 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          x: new Date(10000),
          y: 2,
        },
        {
          x: new Date(20000),
          y: 4,
        },
        {
          x: new Date(30000),
          y: 3,
        },
      ],
    },
  ];
  const data1: { x: Date; y: number }[] = [];
  const [timems, settimems] = useState(Date.now());

  let datasets1 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          x: new Date(timems),
          y: 2,
        },
        {
          x: new Date(timems + 10000),
          y: 4,
        },
        {
          x: new Date(timems + 20000),
          y: 3,
        },
      ],
    },
  ];
  let count = useRef(Date.now());

  const [datasets, setData] = useState(datasets1);
  const [update, setUpdate] = useState("initial");

  function addData() {
    console.log("addData called");

    // settimems(timems + 100000);
    count=count+10000;
    settimems(2);
    console.log("timems " + timems);



    // const value = Math.floor((Math.random() * 10) + 1);
    // datasets1[0].data.splice(0, 1);
    // console.log(datasets1[0].data);
    // datasets[0].data.push({
    //   x: new Date(timems + 30000),
    //   y: value,
    // });
    // console.log("datasets1 " + JSON.stringify(datasets1, null, 4));

    // setData(datasets);

    setUpdate("changed");

    // console.log("datasets " + JSON.stringify(datasets, null, 4));
  }

  const changeData = () => {
    console.log("changeData called");

    settimems(timems + 100000);
    // datasets1[0].data.push({
    //   x: new Date(timems + 30000),
    //   y: 2,
    // });
    // setData(datasets1);
    // console.log("datasets after" + JSON.stringify(datasets, null, 4));
    setUpdate("changed");
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
        requestUpdate={update}
      >
      </LineChartDateMod>
    </div>
  );
}
