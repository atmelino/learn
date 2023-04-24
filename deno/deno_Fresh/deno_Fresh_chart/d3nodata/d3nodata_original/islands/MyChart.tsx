import { BarChart } from "https://deno.land/x/d3nodata@v0.1.3.1/charts.ts";

export default function MyChart() {
  const datasets = [
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
          x: "x2",
        },
      ],
    },
  ];

  return (
    <div>
      <BarChart datasets={datasets} data={datasets[0].data} addTitle={true}></BarChart>
    </div>
  );
}
