import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface debugProps {
  start: number;
  initmessage: string;
}

export default function Debug_user(props: debugProps) {
  const [debugMessage, setdebugMessage] = useState(props.initmessage);

  function setDebugText(message: string) {
    //alert("hi");
    setdebugMessage(message);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <h2 class="text-lg font-medium text-gray-900 ">Debug User</h2>
      This element uses the debug element by sending a message to it<br>
      </br>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(debugMessage + "text")}>
          send debug message
        </Button>
      </div>
    </div>
  );
}
