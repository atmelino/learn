import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";

export default function MyData() {
  let datasets1 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          x: new Date(Date.now()),
          y: 2,
        },
        {
          x: new Date(Date.now() + 10000),
          y: 4,
        },
        {
          x: new Date(Date.now() + 20000),
          y: 3,
        },
      ],
    },
  ];


  return (datasets1  );
}



// let datasets2 = [
//   {
//     label: "test",
//     color: "green",
//     data: [
//       {
//         x: new Date(10000),
//         y: 2,
//       },
//       {
//         x: new Date(20000),
//         y: 4,
//       },
//       {
//         x: new Date(30000),
//         y: 3,
//       },
//     ],
//   },
// ];
