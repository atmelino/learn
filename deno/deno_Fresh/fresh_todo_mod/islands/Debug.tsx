import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface debugProps {
  initmessage: string;
}

export default function Debug(props: debugProps) {
  const [text, setText] = useState("");
  const [debugMessage, setdebugMessage] = useState(props.initmessage);

  function setDebugText(message: string) {
    //alert("hi");
    setdebugMessage(message);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(debugMessage + "text")}>
          debug message
        </Button>
      </div>
      <div>
        <textarea
          class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
        >
          {debugMessage}
        </textarea>
      </div>
    </div>
  );
}
