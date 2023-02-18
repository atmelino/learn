import Debug from "../islands/Debug.tsx";
import Popup from "../islands/Popup.tsx";

export function Body() {
  function myFunction() {
    alert("hi");
  }

  return (
    <header class="h-[110px] sm:!h-[144px] w-full bg-cover bg-no-repeat relative">
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
        <Debug start={1} initmessage="hello" />
      </div>
    </header>
  );
}
