import Debug from "../islands/Debug.tsx";
import Popup from "../islands/Popup.tsx";
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
      <nav class="w-11/12 h-24 max-w-5xl mx-auto flex items-center justify-between relative">
        <h1>
        </h1>
        <Popup
          length={4}
          Url={"http://www.something.com"}
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </nav>

      <div class="p-4 mx-auto max-w-screen-md">
        <Debug
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </div>
      <div class="p-4 mx-auto max-w-screen-md">
        <PeriodicTask
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </div>
    </div>
  );
}
