import { BarChart } from "https://raw.githubusercontent.com/atmelino/d3no-data/main/charts.ts"

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
