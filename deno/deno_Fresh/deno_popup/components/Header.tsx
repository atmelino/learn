import Popup from "../islands/Popup.tsx";

export function Header() {
  return (
    <header
      class="h-[110px] sm:!h-[144px] w-full bg-cover bg-no-repeat relative"
      style={{
        backgroundImage: "url(/header_bg.svg)",
      }}
    >
      <div class="w-full h-full absolute" />
      <nav class="w-11/12 h-24 max-w-5xl mx-auto flex items-center justify-between relative">
        <h1>
          <img
            src="/text_logo.svg"
            alt="Deno Merch"
            class="h-6"
            width="130"
            height="24"
          />
        </h1>
        <Popup />
      </nav>
    </header>
  );
}
//<div class="rainfall w-full h-full absolute" />
