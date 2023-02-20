import { Button } from "../components/Button.tsx";
import * as mydebug from "../islands/Debug.tsx";

interface debugProps {
  start: number;
  initmessage: string;
}

export default function Debug_user(props: debugProps) {

  function setDebugText(message: string) {
    //alert("hi");
    //setdebugMessage(message);
    //mydebug.setAGlobalString("test3");
    mydebug.setAGlobalString(message);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <h2 class="text-lg font-medium text-gray-900 ">Debug User</h2>
      This element uses the debug element by sending a message to it<br>
      </br>
      <div class="flex gap-2 w-full">
      <Button onClick={() => mydebug.setAGlobalString("text from debug user")}>
          send debug message
        </Button>
      </div>
    </div>
  );
}
//<Button onClick={() => setDebugText("text from debug user")}>
