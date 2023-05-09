import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

export default function Body() {
  const [inputValue, setInputValue] = useState("");
  const count = useRef(0);
  const noteRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    count.current = count.current + 1;
  });

  const handleChange = () => {
    setInputValue("!showDebug");
  };


  function createTableFromObjects(data: {}[]) {
    let mystring=""
    const tablestart = ('<table>');
    const tableend = ('</table>');
    const headerRow = ('<tr>');
    const headerEnd = ('<tr>');


    mystring+=tablestart;


    for (var cell of data) {
      console.log(product.product_desc)
 }



    // Create table header row
    const keys = Object.keys(data[0]);
    for (const key of keys) {
      const headerCell = document.createElement('th');
      headerCell.textContent = key;
      headerRow.appendChild(headerCell);
    }
    table.appendChild(headerRow);

    // Create table data rows
    for (const obj of data) {
      const dataRow = document.createElement('tr');
      for (const key of keys) {
        const dataCell = document.createElement('td');
        dataCell.textContent = obj[key];
        dataRow.appendChild(dataCell);
      }
      table.appendChild(dataRow);
    }

    return mystring;
  }

  const dataArray = [
    { id: 1, name: 'John', age: 30 },
    { id: 2, name: 'Jane', age: 28 },
    { id: 3, name: 'Doe', age: 45 },
  ];

  const table = createTableFromObjects(dataArray);



  return (
    <div class="flex flex-col w-full pt-5">
      <div class="flex gap-2 w-full">
        {table}
      </div>


      <div>
        value={inputValue}
      </div>

      <h1>Render Count: {count.current}</h1>
    </div>
  );
}


