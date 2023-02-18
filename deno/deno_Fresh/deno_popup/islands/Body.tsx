import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import Debug from "../islands/Debug.tsx";
import Popup from "../islands/Popup.tsx";


export default function Body() {
  const [debugMessage, setdebugMessage] = useState("new");

  function myFunction() {
    //    alert("hi");
    setDebugText(debugMessage + "by golly it works!");
  }

  function setDebugText(message: string) {
    //alert("hi");
    console.log("test");
    setdebugMessage(debugMessage + "changed");
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <nav class="w-11/12 h-24 max-w-5xl mx-auto flex items-center justify-between relative">
        <h1>
        </h1>
        <Popup
          length={4}
          Url={"http://www.something.com"}
          functionToCall={myFunction}
        />
      </nav>

      <div class="p-4 mx-auto max-w-screen-md">
        <Debug start={1} initmessage="hello" />
      </div>

      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(debugMessage + "text")}>
          debug message in div
        </Button>
      </div>
      <div>
        {debugMessage}
      </div>
      <button
        onClick={() => setdebugMessage("changed")}
        class="flex items-center gap-2 items-center border-2 border-gray-800 rounded-full px-5 py-1 font-semibold text-gray-800 hover:bg-gray-800 hover:text-white transition-colors duration-300"
      >
        test
      </button>
    </div>
  );
}
