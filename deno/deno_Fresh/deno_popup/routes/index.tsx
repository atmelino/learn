import { Head } from "$fresh/runtime.ts";
import Popup from "../islands/Popup.tsx";

export default function Home() {
  //  const p: PopupData = { length: 5, id: "3", Url: "www.something.com" };
  function myFunction(s: string) {
    return ("hello");
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
      x
    </>
  );
}
