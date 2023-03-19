import { useRef, useState } from "preact/hooks";
import { Notes } from "../components/Notes.tsx";
import { Button } from "../components/Button.tsx";
import { Debug2 } from "../components/Debug2.tsx";
import settings from "../../../../../../settings_nk.js";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import { useEffect } from "preact/hooks";
import Popup from "./Popup.tsx";

export interface INote {
  uuid: string;
  timestamp: string;
  desc: string;
}
const dbURL = "http://" + settings.IPsettings.myIPstring + ":7000/todos";

export default function NoteKeeper() {
  const [notes, setNotes] = useState<INote[]>([]);
  const noteRef = useRef<HTMLInputElement | null>(null);
  const [debug, setDebug] = useState("initial");
  const [debugMessage, setdebugMessageState] = useState("123");
  const [showDebug, setShowDebug] = useState(false);

  // Similar to componentDidMount and componentDidUpdate:
  useEffect(() => {
    const date_ob = new Date();
    console.log(format(date_ob, "yyyy-MM-dd HH:mm:ss"));
    console.log("useEffect called");
    readDatabase();
  }, []);

  function setDebugMesssage(message: string) {
    console.log("setDebugMesssage called");
    setdebugMessageState(message);
  }

  function makeRandomId(length: number) {
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

  async function removeNote(uuid: string) {
    console.log("removeNote called");
    setNotes((notes) => notes.filter((note) => note.uuid != uuid));

    console.log("send DELETE request");
    const start = '{"SQL":{';
    const part1 = '"noteId":"';
    const part2 = uuid;
    const end = '"}}';

    const postBody = start + part1 + part2 + end;
    const req = new Request(dbURL, {
      method: "DELETE",
      body: postBody,
    });
    const resp = await fetch(req);
  }

  async function readDatabase() {
    const req = new Request(dbURL, {
      method: "GET",
    });
    const resp = await fetch(req);
    const myData = await resp.text();
    //console.log(await resp.text());
    setNotes([]);
    console.log(myData);
    addDebug(myData);
    const myArr = JSON.parse(myData);
    myArr.forEach((row: any) => {
      console.log(row);
      const uuid = row[2];
      const timestamp = row[1];
      const desc = row[3];
      addNote(uuid, timestamp, desc);
    });
  }

  function addNote(uuid: string, timestamp: string, desc: string) {
    setNotes((
      p,
    ) => [...p, {
      //desc: noteRef?.current?.value ?? "",
      desc: desc,
      timestamp: timestamp,
      uuid: uuid,
    }]);
  }

  async function addNewNote(desc: string) {
    const date_ob = new Date();
    console.log(format(date_ob, "yyyy-MM-dd HH:mm:ss"));
    const timestamp = format(date_ob, "yyyy-MM-dd HH:mm:ss");
    const my_uuid = makeRandomId(10);
    setNotes((
      p,
    ) => [...p, {
      //desc: noteRef?.current?.value ?? "",
      desc: desc,
      timestamp: timestamp,
      uuid: my_uuid,
    }]);
    addDebug(my_uuid);

    console.log("send POST request");

    const start = '{"SQL":{';
    const part1 = '"timestamp":"';
    const part2 = timestamp;
    const part3 = '","noteId":"';
    const part4 = my_uuid;
    const part5 = '","note":"';
    const part6 = desc;
    const end = '"}}';

    const postBody = start + part1 + part2 + part3 + part4 + part5 + part6 +
      end;
    '"}}';
    console.log(postBody);

    const req = new Request(dbURL, {
      method: "POST",
      body: postBody,
    });
    const resp = await fetch(req);
  }

  const Debug = () => (
    <div id="results">
      <Button onClick={() => addNewNote(makeRandomId(8))}>
        add random note
      </Button>
      <Button onClick={() => readDatabase()}>read database</Button>
      <Debug2 debug={debug} />
      <Button onClick={() => addDebug("text")}>debug message</Button>
      <Button onClick={() => addDebug(settings.IPsettings.myIPstring)}>
        my IP string
      </Button>
      s
    </div>
  );

  return (
    <div class="flex flex-col w-full pt-5">
      <form
        class="flex gap-2 w-full"
        onSubmit={(e) => {
          e.preventDefault();

          if (!noteRef?.current?.value) return;
          addNewNote(noteRef?.current?.value ?? "");
          noteRef.current.value = "";
        }}
      >
        <input
          class="w-5/6 border-1 border-gray-500 h-10 rounded p-2"
          defaultValue="test"
          placeholder="Write a new note here..."
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
        <Popup
          title="Settings"
          showDebug={showDebug}
          setShowDebug={setShowDebug}
          setDebugMesssage={setDebugMesssage}
          debugMessage={debugMessage}
        />
      </form>
      <Notes notes={notes} removeNote={removeNote} />

      <div>
        {showDebug ? <Debug /> : null}
      </div>
    </div>
  );
}
