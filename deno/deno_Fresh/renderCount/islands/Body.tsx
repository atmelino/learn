import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

export default function Body() {
  const [inputValue, setInputValue] = useState("");
  const count = useRef(0);
  const noteRef = useRef<HTMLInputElement | null>(null);

  useEffect(() => {
    count.current = count.current + 1;
  });

  const handleChange = () => {
    setInputValue("!showDebug");
  };

  return (
    <div class="flex flex-col w-full pt-5">
      <div class="flex gap-2 w-full">
        <form
          class="flex gap-2 w-full"
          onSubmit={(e) => {
            e.preventDefault();
            if (!noteRef?.current?.value) {
              return;
            }
            setInputValue(noteRef?.current?.value ?? "");
            noteRef.current.value = "";
          }}
        >
          <input
            class="w-5/6 border-1 border-gray-500 h-10 rounded p-2"
            type="text"
            ref={noteRef}
          />
          <Button
            type="submit"
            className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-1/2"
          >
            read
          </Button>
        </form>
      </div>
      <div>
          value={inputValue}
        </div>

      <h1>Render Count: {count.current}</h1>
    </div>
  );
}


