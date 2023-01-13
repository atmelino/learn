import { IDebug } from "../islands/NoteKeeper.tsx";
import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface debugProps {
  debug: IDebug[];
  removeDebug: (s: string) => void;
}

export function Debug({ debug, removeDebug }: debugProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {
        <div>
          <textarea
            class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
          >
            {debug}
          </textarea>
        </div>
      }

      {/* // {notes?.map((note) => <Note note={note} removeNote={removeNote} />)} */}
    </div>
  );
}

// export function Debug({ message, removeNote }: debugProps) {
//   const [debugMessage, setdebugMessage] = useState(message);

//   function setDebugText(message: string) {
//     //alert("hi");
//     setdebugMessage(message);
//   }

//   return (
//     <div class="flex flex-col w-full pt-5">
//       <div class="flex gap-2 w-full">
//         <Button onClick={() => setDebugText(debugMessage + "text")}>
//           debug message
//         </Button>
//       </div>
//       <div>
//         <textarea
//           class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
//         >
//           {debugMessage}
//         </textarea>
//       </div>
//     </div>
//   );
// }
