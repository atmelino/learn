import { useRef, useState } from "preact/hooks";
import { IS_BROWSER } from "$fresh/runtime.ts";
import { apply, tw } from "twind";
import { animation, css } from "twind/css";
import IconSettings from "../components/IconSettings.tsx";
import { Button } from "../components/Button.tsx";

interface PopupProps {
  title: string;
  showDebug: boolean;
  setShowDebug: (s: boolean) => void;
  setDebugMesssage: (s: string) => void;
  debugMessage: string;
  yAxisAuto:boolean
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

export default function Popup(
  { title, showDebug, setShowDebug, setDebugMesssage, debugMessage,yAxisAuto }:
    PopupProps,
) {
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
        <PopupInner
          title={title}
          showDebug={showDebug}
          setShowDebug={setShowDebug}
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
          yAxisAuto={yAxisAuto}

        />
      </dialog>
    </div>
  );
}

function PopupInner(
  { title, showDebug, setShowDebug, setDebugMesssage, debugMessage,yAxisAuto }: PopupProps,
) {
  const [checked, setChecked] = useState(false);
  const [disabled, setDisabled] = useState(" text-gray-300");

  const corners = "rounded(tl-2xl tr-2xl sm:(tr-none bl-2xl))";
  const card =
    `py-8 px-6 h-full bg-white ${corners} flex flex-col justify-between`;

    // const handleChange = () => {
    //   setShowDebug(!showDebug);
    // };

    const handleChange = () => {
      console.log("handleChange called")
      yAxisAuto.current = !yAxisAuto.current;
      // setField("border border-solid border-red-300 p-3 space-x-3 text-gray-300");
      // if(yAxisAuto.current)
      setDisabled(yAxisAuto.current ? "text-black" : " text-gray-300");
    };
  
  return (
    <div class={card}>
      <div class="flex justify-between">
        <h2 class="text-lg font-medium text-gray-900">{title}</h2>
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
        <label>
          <input
            type="checkbox"
            onChange={handleChange}
          />
          Show Debug Interface
        </label>

        <fieldset class="border border-solid border-gray-300 p-2 rounded space-x-3"
          disabled={yAxisAuto.current}
        >
          <legend class="text-sm space-x-3">
            y-Axis Scale<label>   </label><input type="checkbox" checked={yAxisAuto.current} onChange={handleChange} />
            <label class={disabled}>auto</label>
          </legend>
          <div class={yAxisAuto.current ? " text-gray-300" : "text-black"} disabled={yAxisAuto.current}>
            <label>  Min  </label>
            <input
              class={"w-1/6 border-1 border-gray-500 h-8 rounded p-2"}
              disabled={yAxisAuto.current}
              type="number"
              id="min"
              min="0" max="100000"
              ref={minRef}
            />
            <label>   Max  </label>
            <input
              class="w-1/6 border-1 border-gray-500 h-8 rounded p-2"
              disabled={yAxisAuto.current}
              type="number"
              id="max"
              min="0" max="100000"
              ref={maxRef}
            />
            <label>     </label>
            <Button
              class={yAxisAuto.current ? "text-gray-300" : "text-black"} disabled={yAxisAuto.current}
              onClick={clickSet}
            >Set
            </Button>
          </div>
        </fieldset>




      </div>
    </div>
  );
}
