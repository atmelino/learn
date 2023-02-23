import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { Button } from "../components/Button.tsx";
import { MyIP } from "../components/MyIP.tsx";

interface debugProps {
  start: number;
  initmessage: string;
  newmessage:string
}

declare global {
  export let MyGlobalString: string;
}
let MyGlobalString = "new";

export function setMyGlobalString(newcontent: string) {
  console.log("setMyGlobalString called");
  MyGlobalString = newcontent;
}

export default function Debug(props: debugProps) {
  const [message_in_div, setmessage_in_div] = useState(props.initmessage);
  const [message_in_textarea, setmessage_in_textarea] = useState(props.initmessage);
  const [message_in_textarea_component, setmessage_in_textarea_component] = useState(props.initmessage);
  const [myIPstring, setDebug] = useState("initial");

  function setDebugText(message: string) {
    //alert("hi");
    setMyGlobalString("test2");
    setmessage_in_div(message);
  }

  function setDebugmessage_in_textarea(message: string) {
    //alert("hi");
    setmessage_in_textarea(MyGlobalString);
  }

  return (
    <div class="flex flex-col w-full ">
      <h2 class="text-lg font-medium text-gray-900 ">Debug Widget</h2>

      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugText(message_in_div + "text")}>
          debug message in div
        </Button>
      </div>
      <div>
        {message_in_div}
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setDebugmessage_in_textarea(message_in_textarea + "text")}>
          debug message in textarea
        </Button>
      </div>
      <div>
        <textarea
          class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
        >
          {message_in_textarea}
        </textarea>
      </div>
      <div class="flex gap-2 w-full">
        <Button onClick={() => setmessage_in_textarea_component(message_in_textarea_component + "text")}>
          debug message in Textarea component
        </Button>
      </div>
      <TextArea
        placeholder="text here..."
        rows={3}
        onChange={(e) => setmessage_in_textarea_component((e.target as HTMLInputElement).value)}
      />
      <MyIP myIPstring={myIPstring} />
    </div>
  );
}
