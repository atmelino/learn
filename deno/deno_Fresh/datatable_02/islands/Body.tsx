import { useEffect, useRef, useState } from "preact/hooks";
import DataTable from "../islands/DataTable.tsx";

export default function Body() {
  const dataArray = [
    { id: 1, name: "John", age: 30, rand: 0 },
    { id: 2, name: "Jane", age: 28, rand: 3 },
    { id: 3, name: "Doe", age: 45, rand: 4 },
    { id: 4, name: "Cindy", age: 35, rand: 1 },
  ];

  // console.log(JSON.stringify(dataArray));

  return (
    <div class="flex flex-row justify-evenly">

      <DataTable
        dataArray={dataArray}
      />

    </div>
  );
}
