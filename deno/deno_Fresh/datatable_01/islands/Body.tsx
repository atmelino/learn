import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

export default function Body() {
  const [cellValue, setCellValue] = useState("");
  const count = useRef(0);
  const rows = 0;
  const cols = 0;
  const dataArray = [
    { id: 1, name: 'John', age: 30 },
    { id: 2, name: 'Jane', age: 28 },
    { id: 3, name: 'Doe', age: 45 },
  ];



  for (const data of dataArray) {
    // console.log(data);
    // console.log(data.name);
    const keys = Object.keys(data);
    for (const key of keys) {
      console.log(key);

      // console.log(data[key]);

    }

  }




  useEffect(() => {
    count.current = count.current + 1;
  });


  function createTableFromObjects(data: {}[]) {
    let mystring = ""
    const tablestart = ('<table>');
    const tableEnd = ('</table>');
    const rowStart = ('<tr>');
    const rowEnd = ('</tr>');
    const cellStart = "<td>";
    const cellEnd = "</td>";


    mystring += tablestart;

    for (const cell of data) {
      // console.log(cell);

      mystring += rowStart;
      const keys = Object.keys(data[0]);
      // console.log(keys);
      // let key: keyof typeof cell;
      for (const key of keys) {
        mystring += cellStart;
        // console.log(key);
        // console.log(key);
        mystring += cellEnd;


      }
      mystring += rowEnd;
    }

    mystring += tableEnd;


    // // Create table header row
    // const keys = Object.keys(data[0]);
    // for (const key of keys) {
    //   const headerCell = document.createElement('th');
    //   headerCell.textContent = key;
    //   headerRow.appendChild(headerCell);
    // }
    // table.appendChild(headerRow);

    // // Create table data rows
    // for (const obj of data) {
    //   const dataRow = document.createElement('tr');
    //   for (const key of keys) {
    //     const dataCell = document.createElement('td');
    //     dataCell.textContent = obj[key];
    //     dataRow.appendChild(dataCell);
    //   }
    //   table.appendChild(dataRow);
    // }

    return mystring;
  }


  const table = createTableFromObjects(dataArray);







  return (
    <div class="flex flex-col w-full pt-5">
      <div class="flex gap-2 w-full">
        {table}
      </div>

      <div class="flex gap-2 w-full">
        {{ table }}
      </div>

      <div class="flex gap-2 w-full">
        <table class="border-collapse border border-slate-400 ...">

          {
            [1, 2, 3, 4, 5, 6].map((value, index) => {
              return <div key={index}>{value}</div>
            })
          }

          {
            [1, 2, 3, 4, 5, 6].map((value, index) => {
              return <tr key={index}>{value}
                <td>Alfreds Futterkiste</td>
                <td>{value}</td>
              </tr>
            })
          }




        </table>
      </div>

    </div>
  );
}


