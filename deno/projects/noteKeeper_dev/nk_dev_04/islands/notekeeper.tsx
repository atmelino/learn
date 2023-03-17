import { Remult } from "remult";
import { useState } from "preact/hooks";
import { Note } from "../model/note.ts";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import { Button } from "../components/Button.tsx";

const remult = new Remult();
const noteRepo = remult.repo(Note);

export default function Notekeeper({ data }: { data: Note[] }) {
  const [notes, setNotes] = useState<Note[]>(data);

  const printNotes = () => {
    console.log(JSON.stringify(notes, null, 4));
    const sortedNotes = notes.sort((a, b) =>
      (a.timestamp < b.timestamp) ? -1 : 1
    );
    console.log(JSON.stringify(sortedNotes, null, 4));
  };

  const addNote = () => {
    setNotes([...notes, new Note()]);
  };

  function getDate() {
    const date_ob = new Date();
    console.log(format(date_ob, "yyyy-MM-dd HH:mm:ss"));
    const timestamp = format(date_ob, "yyyy-MM-dd HH:mm:ss");
    return timestamp;
  }

  function formatDate(date_ob: Date) {
    console.log(format(date_ob, "yyyy-MM-dd HH:mm:ss"));
    const timestamp = format(date_ob, "yyyy-MM-dd HH:mm:ss");
    return timestamp;
  }

  return (
    <div class="flex flex-col gap-1 w-full">
      {notes.map((note) => {
        const handleChange = (values: Partial<Note>) => {
          note.timestamp = getDate();
          setNotes(notes.map((t) => t === note ? { ...note, ...values } : t));
        };

        const saveNote = async () => {
          console.log(formatDate(new Date(note.timestamp)));
          const savedNote = await noteRepo.save(note);
          setNotes(notes.map((t) => t === note ? savedNote : t));
        };

        const deleteNote = async () => {
          await noteRepo.delete(note);
          setNotes(notes.filter((t) => t !== note));
        };

        return (
          <div class="flex gap-4 w-full" key={note.id}>
            <p class="p-2 w-1/6">
              {formatDate(new Date(note.timestamp))}
            </p>
              <input class="flex-grow-1 w-full p-2 text-xl rounded shadow bg-gray-50"
                value={note.note}
                onInput={(e) => handleChange({ note: e.currentTarget.value })}
              />
            <Button onClick={saveNote}>Save</Button>
            <Button onClick={deleteNote}>Delete</Button>
          </div>
        );
      })}
      <Button onClick={addNote}>Add Note</Button>
      <Button onClick={printNotes}>Print Notes</Button>
    </div>
  );
}
