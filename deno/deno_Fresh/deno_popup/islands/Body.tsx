import Debug from "../islands/Debug.tsx";
import Popup from "../islands/Popup.tsx";
import { useRef, useState } from "preact/hooks";

export default function Body() {
  function setDebugMesssage(message: string) {
    console.log("setDebugMesssage called");
    setdebugMessageState(message);
  }

  const [debugMessage, setdebugMessageState] = useState("123");

  return (
    <>
      <div class="flex flex-row justify-evenly">
        <label class="w-5/6 flex justify-center  text-lg font-medium text-gray-900 ">
          Popup Window Demonstrator
        </label>

        <Popup
          length={4}
          Url={"http://www.something.com"}
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </div>

      <div class="p-4 mx-auto max-w-screen-md">
        <Debug
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </div>
    </>
  );
}
