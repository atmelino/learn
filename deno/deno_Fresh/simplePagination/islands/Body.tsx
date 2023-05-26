import { useEffect, useRef, useState } from "preact/hooks";
// import { DataTable } from "../../../../../../DataTable_dev/mod.ts";
import DataTable from "./DataTable.tsx";
import MyData from "./myData.tsx";

export default function Body() {
  const [myData, setMyData] = useState(MyData);

  return (
    <>
      <div class="flex flex-row justify-evenly">
        <DataTable
          dataArray={myData}
        />
      </div>
    </>
  );
}
