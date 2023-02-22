import { Button } from "../components/Button.tsx";
import { getIP } from "https://deno.land/x/get_ip/mod.ts";
import { useRef, useState } from "preact/hooks";

interface myIPProps {
  myIPstring: string;
}

export function MyIP({ myIPstring }: myIPProps) {
  const [dbread, setdbRead] = useState("database");

  const getMyIP = async () => {
    console.log("getmyIP");
    const myIP = await getIP({ ipv6: true });
    console.log(myIP);
    setdbRead(myIP+"");    
    return myIP;
  };
  
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {
        <div>
          <Button  onClick={async () => await getMyIP()}>
            get IP
          </Button>

          <textarea
            class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
          >
            {dbread}
          </textarea>
        </div>
      }
    </div>
  );
}

//onLoad={() => console.log("hi")}
//<Button  onClick={() => init()}>
