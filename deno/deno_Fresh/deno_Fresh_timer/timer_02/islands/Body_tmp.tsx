import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import PeriodicTask from "../islands/PeriodicTask.tsx";

export default function Body() {
  const [debugMessage, setdebugMessage] = useState("new");

  function setDebugText(message: string) {
    //alert("hi");
    console.log("test");
    setdebugMessage(debugMessage + "changed");
  }

  function addData() {
    console.log("addData called");

    return;
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <div class="p-4 mx-auto max-w-screen-md">
      </div>

      <div>
        {/* <PeriodicTask name="chart update" TaskName={addData}>
          <span>Click me</span>
        </PeriodicTask> */}
      </div>

      <button onClick={() => addData()}>Add Data</button>
    </div>
  );
}
