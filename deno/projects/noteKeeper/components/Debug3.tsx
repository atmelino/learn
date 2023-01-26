import { Button } from "../components/Button.tsx";
import { getIP } from "https://deno.land/x/get_ip/mod.ts";
import { useRef, useState } from "preact/hooks";

interface debugProps {
  debug: string;
}

const getMyIP = async () => {
  console.log("getmyIP");
  const myIP = await getIP({ ipv6: true });
  console.log(myIP);
  return myIP;
};


export function Debug3({ debug }: debugProps) {
  const [dbread, setdbRead] = useState("database");
  //const myIP = getMyIP();
  function init() {
    console.log("clicked");
    const myIP= getMyIP()
    setdbRead(myIP+"");
    return getMyIP()
  }
  
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {
        <div>
          <Button  onClick={() => init()}>
            debug message
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