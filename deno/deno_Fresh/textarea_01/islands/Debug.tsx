import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { Button } from "../components/Button.tsx";

interface debugProps {
  start: number;
  initmessage: string;
}

export default function Debug(props: debugProps) {
  const [text, setText] = useState(props.initmessage);
  const [debugMessage, setdebugMessage] = useState(props.initmessage);

  function setDebugText1(message: string) {
    //alert("hi");
    setText(message);
  }

  function setDebugText(message: string) {
    //alert("hi");
    setdebugMessage(message);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <TextArea
        placeholder="text here..."
        rows={15}
        onChange={(e) => setText((e.target as HTMLInputElement).value)}
      />
      <div>
        {debugMessage}
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(debugMessage + "text")}>
          debug message in div
        </Button>
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText1(text + "text")}>
          debug message in textarea
        </Button>
      </div>
      <div>
        <textarea
          class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
        >
          {text}
        </textarea>
      </div>
    </div>
  );
}
