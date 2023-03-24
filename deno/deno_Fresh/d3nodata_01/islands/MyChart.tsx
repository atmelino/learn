import { useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { BarChart } from "https://deno.land/x/d3nodata@v0.1.3.1/charts.ts";

export default function MyChart() {
  const fakedata1 = [
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
      ],
    },
  ];
  const fakedata2 = [
    {
      label: "test",
      color: "blue",
      data: [
        {
          y: 4,
          x: "x1",
        },
        {
          y: 5,
          x: "x2",
        },
      ],
    },
  ];
  const other = [
    {
      y: 2,
      x: "x1",
    },
  ];

  const [data, setData] = useState(fakedata1);

  let boolval = true;

  const addNote = () => {
    console.log("addNote called");
    //console.log(JSON.stringify(fakedata1, null, 4));
    //console.log(JSON.stringify(fakedata2, null, 4));

    //console.log(JSON.stringify(fakedata, null, 4));
    //fakedata[0].data[0].y=7;
    //console.log(JSON.stringify(fakedata, null, 4));

    console.log(JSON.stringify(data, null, 4));
    setData(fakedata2);
    console.log(JSON.stringify(data, null, 4));
    //BarChart.cleanDatasets()
    //setmynumbers(numbers(barCfg));
    //mynumbers = numbers(barCfg);
    console.log(boolval);
    boolval = false;
    console.log(boolval);
  };

  return (
    <div>
      <div>
        <Button onClick={addNote}>Add Note</Button>
        {JSON.stringify(data, null, 4)}
      </div>
      <BarChart datasets={data} data={other} addTitle={boolval}></BarChart>
    </div>
  );
}
