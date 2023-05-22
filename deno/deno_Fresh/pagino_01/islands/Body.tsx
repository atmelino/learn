import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import Pagino from 'https://raw.githubusercontent.com/pagino/pagino-js/main/src/index.ts';

export default function Body() {
  const [cellValue, setCellValue] = useState("");
  const count = useRef(0);
  const rows = 0;
  const cols = 0;
  const dataArray = [
    { id: 1, name: "John", age: 30, rand: 0 },
    { id: 2, name: "Jane", age: 28, rand: 3 },
    { id: 3, name: "Doe", age: 45, rand: 4 },
    { id: 4, name: "Cindy", age: 35, rand: 1 },
  ];


  for (const data of dataArray) {
    const someObj = data;
    const keys = Object.keys(data);
    for (const key of keys) {
      const temp = someObj[key as keyof typeof someObj];
    }
  }

  useEffect(() => {
    count.current = count.current + 1;
  });

  const keys = Object.keys(dataArray[0]);

  return (
    <div class="flex gap-2 w-full">
      <table class="border-2">
        <tr class="border-2">
          {keys.map((data, index) => {
            return <th class="border-2">{keys[index]}</th>;
          })}
        </tr>

        {dataArray.map((data, index) => {
          return (
            <tr class="border-2" key={index}>
              {keys.map((k) => {
                return (
                  <td class="border-2">{data[k as keyof typeof data]}</td>
                );
              })}
            </tr>
          );
        })}

      </table>
    </div>
  );
}
