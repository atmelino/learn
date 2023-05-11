import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

export default function Body() {
  const [cellValue, setCellValue] = useState("");
  const count = useRef(0);
  const rows = 0;
  const cols = 0;
  const dataArray = [
    { id: 1, name: 'John', age: 30 ,rand: 0},
    { id: 2, name: 'Jane', age: 28 ,rand: 3},
    { id: 3, name: 'Doe', age: 45 ,rand: 4},
  ];

  // console.log(JSON.stringify(dataArray));

  for (const data of dataArray) {
    const keys = Object.keys(data);
    console.log("The use of map is as follows=");
    keys.map(k => { console.log(data[k as keyof typeof data]) })
  }


  for (const data of dataArray) {
    // console.log(data);
    // console.log(data.name);
    const someObj = data;
    const keys = Object.keys(data);
    for (const key of keys) {
      const temp = someObj[key as keyof typeof someObj]
      // console.log(key + " : " + temp);
    }
  }

  useEffect(() => {
    count.current = count.current + 1;
  });




  return (
    <div class="flex flex-col w-full pt-5">

      <div class="flex gap-2 w-full">
        <table class="border-2">
          {
            dataArray.map((data, index) => {
              // console.log(value);
              const keys = Object.keys(data);

              return <tr class="border-2" key={index}>{data}
                {
                  keys.map(k => {

                    // <td>{data[k as keyof typeof data]}</td>

                    console.log(data[k as keyof typeof data])

                    return <td  class="border-2">{data[k as keyof typeof data]}</td>


                  })
                }
              </tr>
            })
          }
        </table>
      </div>



      <div class="flex gap-2 w-full">
        <table class="border-2">
          {
            dataArray.map((value, index) => {
              // console.log(value);
              return <tr class="border-2" key={index}>{value}
                <td>cell content</td>
                <td>{value}</td>
                <td class="border-2" >{JSON.stringify(value)}</td>
              </tr>
            })
          }
        </table>
      </div>

      <div class="flex gap-2 w-full">
        <table class=" border-2">
          {
            [1, 2, 3, 4, 5, 6].map((value, index) => {
              return <div key={index}>{value}</div>
            })
          }
        </table>
      </div>

    </div>
  );
}


