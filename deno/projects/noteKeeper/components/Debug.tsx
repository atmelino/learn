import { IDebug } from "../islands/NoteKeeper.tsx";

interface debugProps {
  debug: IDebug[];
  removeNote: (s: string) => void;
}

export function Debug({ debug, removeNote }: debugProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {
        <div>
          <textarea
            class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
          >
            "hi"
          </textarea>
        </div>
      }
    </div>
  );
  //{debug}
  //{notes?.map((note) => <Note note={note} removeNote={removeNote} />)}
}
