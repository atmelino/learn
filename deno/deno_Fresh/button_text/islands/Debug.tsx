import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface debugProps {
  start: number;
  initmessage: string;
}

export default function Debug(props: debugProps) {
  const [text, setText] = useState("");
  const [count, setCount] = useState(props.start);
  const [debugMessage, setdebugMessage] = useState(props.initmessage);

  function setDebugText(message: string) {
    //alert("hi");
    setdebugMessage(message);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <div>
        {debugMessage}
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(debugMessage + "text")}>
          debug message
        </Button>
      </div>
      <div>
      </div>
    </div>
  );
}
