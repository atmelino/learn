import { useRef, useState } from "preact/hooks";
import { Notes } from "../components/Notes.tsx";
import { Button } from "../components/Button.tsx";
import { Debug } from "../components/Debug.tsx";
import { Debug2 } from "../components/Debug2.tsx";
import { dbRead } from "../components/dbRead.tsx";

export interface INote {
  uuid: string;
  desc: string;
}

export default function NoteKeeper() {
  const [notes, setNotes] = useState<INote[]>([]);
  const noteRef = useRef<HTMLInputElement | null>(null);
  const [debug, setDebug] = useState("initial");
  let my_uuid = "";

  function makeid(length: number) {
    let result = "";
    const characters =
      "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
      result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
  }

  function addDebug(message: string) {
    setDebug(message);
  }

  function removeNote(uuid: string) {
    setNotes((notes) => notes.filter((note) => note.uuid != uuid));
  }

  function addNote(uuid: string) {
    //setDebugText();
    //my_uuid=crypto.randomUUID();
    my_uuid = makeid(36);
    //my_uuid = Math.random() * 10000;
    setNotes((
      p,
    ) => [...p, {
      desc: noteRef?.current?.value ?? "",
      uuid: my_uuid,
    }]);
    addDebug(my_uuid);
  }

  return (
    <div class="flex flex-col w-full pt-5">
      <form
        class="flex gap-2 w-full"
        onSubmit={(e) => {
          e.preventDefault();

          if (!noteRef?.current?.value) return;
          addNote("");
          // setNotes((
          //   p,
          // ) => [...p, {
          //   desc: noteRef?.current?.value ?? "",
          //   uuid: crypto.randomUUID(),
          // }]);
          noteRef.current.value = "";
        }}
      >
        <input
          class="w-5/6 border-1 border-gray-500 h-10 rounded p-2"
          defaultValue="test"
          placeholder="Write your note here..."
          type="text"
          ref={noteRef}
        />
        <button
          type="submit"
          // value="Add"
          class="w-1/6 bg-gray-200 text-gray-50 rounded cursor-pointer hover:bg-gray-300 flex justify-center items-center"
        >
          <svg
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
            class="w-6"
          >
            <path d="M410.3 231l11.3-11.3-33.9-33.9-62.1-62.1L291.7 89.8l-11.3 11.3-22.6 22.6L58.6 322.9c-10.4 10.4-18 23.3-22.2 37.4L1 480.7c-2.5 8.4-.2 17.5 6.1 23.7s15.3 8.5 23.7 6.1l120.3-35.4c14.1-4.2 27-11.8 37.4-22.2L387.7 253.7 410.3 231zM160 399.4l-9.1 22.7c-4 3.1-8.5 5.4-13.3 6.9L59.4 452l23-78.1c1.4-4.9 3.8-9.4 6.9-13.3l22.7-9.1v32c0 8.8 7.2 16 16 16h32zM362.7 18.7L348.3 33.2 325.7 55.8 314.3 67.1l33.9 33.9 62.1 62.1 33.9 33.9 11.3-11.3 22.6-22.6 14.5-14.5c25-25 25-65.5 0-90.5L453.3 18.7c-25-25-65.5-25-90.5 0zm-47.4 168l-144 144c-6.2 6.2-16.4 6.2-22.6 0s-6.2-16.4 0-22.6l144-144c6.2-6.2 16.4-6.2 22.6 0s6.2 16.4 0 22.6z" />
          </svg>
        </button>
      </form>
      <Button onClick={() => addDebug("text")}>debug message</Button>
      <Debug debug={debug} />
      <Notes notes={notes} removeNote={removeNote} />
      <Button onClick={() => addNote("text")}>add a new note</Button>
      <Debug2 debug={debug} />
    </div>

  );
}
