import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { Button } from "../components/Button.tsx";

interface debugProps {
  start: number;
  initmessage: string;
}

export default function Debug(props: debugProps) {
  const [text, setText] = useState("");
  const [count, setCount] = useState(props.start);
  const [debugMessage, setdebugMessage] = useState(props.initmessage);


  function setDebugText1(message: string) {
    alert("hi");
    setText(message);
  }

  function setDebugText(message: string) {
    //alert("hi");
    setdebugMessage(message);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <TextArea
        placeholder="Paste your code or text here..."
        rows={15}
        onChange={(e) => setText((e.target as HTMLInputElement).value)}
      />
      <div>
        {debugMessage}
      </div>
      <div class="flex gap-2 w-full">
        <p class="flex-grow-1 font-bold text-xl">{count}</p>
        <Button onClick={() => setCount(count - 1)}>-1</Button>
        <Button onClick={() => setText(count + "1")}>+1</Button>
        <Button onClick={() => setDebugText(debugMessage+"text")}>debug message</Button>
      </div>
      <div>
      <textarea
			class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
      >hello</textarea>
      /</div>
    </div>
  );
}
