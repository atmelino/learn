import Debug from "../islands/Debug.tsx";
import { useRef, useState } from "preact/hooks";
import PeriodicTask from "./PeriodicTask.tsx";

export default function Body() {
  function setDebugMesssage(message: string) {
    console.log("setDebugMesssage called");
    setdebugMessageState(message);
  }

  const [debugMessage, setdebugMessageState] = useState("123");

  return (
    <div class="flex flex-col w-full pt-5">

      <div class="p-4 mx-auto max-w-screen-md">
        <Debug
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </div>
      <div class="p-4 mx-auto max-w-screen-md">
        <PeriodicTask
          TaskName={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </div>
    </div>
  );
}
