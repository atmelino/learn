import { useRef, useState } from "preact/hooks";
import { IS_BROWSER } from "$fresh/runtime.ts";
import { apply, tw } from "twind";
import { animation, css } from "twind/css";
import IconSettings from "../components/IconSettings.tsx";

interface PopupProps {
  length: number;
  Url: string;
  //functionToCall: (s: string) => void;
  functionToCall: () => void;
}

// Lazy load a <dialog> polyfill.
// @ts-expect-error HTMLDialogElement is not just a type!
if (IS_BROWSER && window.HTMLDialogElement === "undefined") {
  await import(
    "https://raw.githubusercontent.com/GoogleChrome/dialog-polyfill/5033aac1b74c44f36cde47be3d11f4756f3f8fda/dist/dialog-polyfill.esm.js"
  );
}

declare global {
  interface HTMLDialogElement {
    showModal(): void;
    close(): void;
  }
}

const slideRight = animation("0.4s ease normal", {
  from: { transform: "translateX(100%)" },
  to: { transform: "translateX(0)" },
});

const slideBottom = animation("0.4s ease normal", {
  from: { transform: "translateY(100%)" },
  to: { transform: "translateY(0)" },
});

const backdrop = css({
  "&::backdrop": {
    background: "rgba(0, 0, 0, 0.5)",
  },
});

export default function Popup({ length, Url, functionToCall }: PopupProps) {
  const ref = useRef<HTMLDialogElement | null>(null);

  const onDialogClick = (e: MouseEvent) => {
    if ((e.target as HTMLDialogElement).tagName === "DIALOG") {
      ref.current!.close();
    }
  };

  return (
    <div>
      <button
        onClick={() => ref.current!.showModal()}
        class="flex items-center gap-2 items-center border-2 border-gray-800 rounded-full px-5 py-1 font-semibold text-gray-800 hover:bg-gray-800 hover:text-white transition-colors duration-300"
      >
        <IconSettings size={20} />
      </button>
      <dialog
        ref={ref}
        class={tw`bg-transparent p-0 m-0 pt-[50%] sm:pt-0 sm:ml-auto max-w-full sm:max-w-lg w-full max-h-full h-full ${slideBottom} sm:${slideRight} ${backdrop}`}
        onClick={onDialogClick}
      >
        <PopupInner length={length} Url={Url} functionToCall={functionToCall} />
      </dialog>
    </div>
  );
}

function PopupInner({ length, Url, functionToCall }: PopupProps) {
  const [text_ta, setText_ta] = useState("initial text");

  const corners = "rounded(tl-2xl tr-2xl sm:(tr-none bl-2xl))";
  const card =
    `py-8 px-6 h-full bg-white ${corners} flex flex-col justify-between`;

  const goToUrl = (e: Event) => {
    e.preventDefault();
    location.href = Url;
  };

  // const callAFunction = (e: Event) => {
  //   e.preventDefault();
  //   functionToCall;
  // };

  const callAFunction = (e: Event) => {
    e.preventDefault();
    setDebugText_ta("new text");
  };

  function setDebugText_ta(message: string) {
    //alert("hi");
    setText_ta(message);
  }

  return (
    <div class={card}>
      <div class="flex justify-between">
        <h2 class="text-lg font-medium text-gray-900">Popup window</h2>
        <button
          class="py-1"
          onClick={(e) => {
            (e.target as HTMLButtonElement).closest("dialog")!.close();
          }}
        >
          <svg
            class="w-6 h-6 fill-current text-gray-600"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path d="M19 6.41L17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12z" />
          </svg>
        </button>
      </div>
      <div class="flex-grow-1 my-4">
      </div>
      <div>
        <textarea
          class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
        >
          {text_ta}
        </textarea>
      </div>

      <div class="mt-6">
        <button
          type="button"
          class="w-full bg-gray-700 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-gray-700"
          onClick={callAFunction}
        >
          call a function
        </button>
      </div>

      <div class="border-t border-gray-200 py-6 px-4 sm:px-6">
        <div class="flex justify-between text-lg font-medium">
          <p>A Number:</p>
          <p>{length}</p>
        </div>
        <div class="mt-6">
          <button
            type="button"
            class="w-full bg-gray-700 border border-transparent rounded-md py-3 px-8 flex items-center justify-center text-base font-medium text-white hover:bg-gray-700"
            onClick={goToUrl}
          >
            Go to a URL
          </button>
        </div>
      </div>
    </div>
  );
}
