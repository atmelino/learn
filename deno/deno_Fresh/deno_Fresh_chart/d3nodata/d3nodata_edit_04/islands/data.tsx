import { now } from "https://esm.sh/v112/@types/d3-timer@3.0.0/index";
import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { LineChartDateMod } from "../library/charts.ts";

export default function MyData() {
  const timems = Date.now();
  const datasets1 = [
    {
      label: "test",
      color: "green",
      data: [
        {
          x: timems,
          y: 2,
        },
        {
          x: timems + 10000,
          y: 4,
        },
        {
          x: timems + 20000,
          y: 3,
        },
        {
          x: timems + 40000,
          y: 5,
        },
        {
          x: timems + 50000,
          y: 3,
        },
      ],
    },
  ];

  return (datasets1);
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
