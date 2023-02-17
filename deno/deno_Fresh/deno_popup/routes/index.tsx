import { Head } from "$fresh/runtime.ts";
import { useRef, useState } from "preact/hooks";
import Popup from "../islands/Popup.tsx";
import { Button } from "../components/Button.tsx";

export default function Home() {
  const [text_ta, setText_ta] = useState("initial text");
  let myText = "my text";

  // function myFunction(s: string) {
  //   myText = "changed text";
  // }

  function myFunction() {
    alert("hi");
    setDebugText_ta("new text");
  }

  function setDebugText_ta(message: string) {
    //alert("hi");
    setText_ta(message);
  }

  return (
    <>
      <Head>
        <title>deno popup demo</title>
      </Head>
      <div class="w-full h-full absolute" />
      <nav class="w-11/12 h-24 max-w-5xl mx-auto flex items-center justify-between relative">
        <h1>
        </h1>

        <Popup
          length={4}
          Url={"http://www.something.com"}
          functionToCall={myFunction}
        />
      </nav>

      <div class="p-4 mx-auto max-w-screen-md">
        <p class="my-6">
          Click on the settings icon to open the popup window
        </p>
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
    </>
  );
}
