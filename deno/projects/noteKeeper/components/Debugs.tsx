import { IDebug } from "../islands/NoteKeeper.tsx";
import { Debug } from "./Debug.tsx";

interface debugProps {
  debugs: IDebug[];
  removeNote: (s: string) => void;
}

export function Debugs({ debugs, removeNote }: debugProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {debugs?.map((note) => <Debug note={note} removeNote={removeNote} />)}
    </div>
  );
  //{debug}
  //{notes?.map((note) => <Note note={note} removeNote={removeNote} />)}

//   <div class="flex flex-col gap-2 pt-2 w-full">
//   {
//     <div>
//       <textarea
//         class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
//       >
//         "hi"
//       </textarea>
//     </div>
//   }
// </div>

}
