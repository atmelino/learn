import Debug from "../islands/Debug.tsx";
import Popup from "../islands/Popup.tsx";

export default function Body() {

  return (
    <div class="flex flex-col w-full pt-5">
      <nav class="w-11/12 h-24 max-w-5xl mx-auto flex items-center justify-between relative">
        <h1>
        </h1>
        <Popup
          length={4}
          Url={"http://www.something.com"}
        />
      </nav>

      <div class="p-4 mx-auto max-w-screen-md">
      <Debug start={1} initmessage="hello" newmessage="init" />
      </div>

    </div>
  );
}
