import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { Button } from "../components/Button.tsx";
import { MyIP } from "../components/MyIP.tsx";

interface debugProps {
  start: number;
  initmessage: string;
}

export default function Debug(props: debugProps) {
  const [debugMessage, setdebugMessage] = useState(props.initmessage);
  const [text_ta, setText_ta] = useState(props.initmessage);
  const [text_tac, setText_tac] = useState(props.initmessage);
  const [debug, setDebug] = useState("initial");

  function setDebugText(message: string) {
    //alert("hi");
    setdebugMessage(message);
  }

  function setDebugText_ta(message: string) {
    //alert("hi");
    setText_ta(message);
  }

  return (
    <div class="flex flex-col w-full ">
      <h2 class="text-lg font-medium text-gray-900 ">Debug Widget</h2>

      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(debugMessage + "text")}>
          debug message in div
        </Button>
      </div>
      <div>
        {debugMessage}
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText_ta(text_ta + "text")}>
          debug message in textarea
        </Button>
      </div>
      <div>
        <textarea
          class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
        >
          {text_ta}
        </textarea>
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setText_tac(text_tac + "text")}>
          debug message in Textarea component
        </Button>
      </div>
      <TextArea
        placeholder="text here..."
        rows={3}
        onChange={(e) => setText_tac((e.target as HTMLInputElement).value)}
      />
      <MyIP debug={debug} />
    </div>
  );
}
