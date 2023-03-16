import { Remult } from "remult";
import { useState } from "preact/hooks";
import { Note } from "../model/note.ts";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import { Button } from "../components/Button.tsx";

const remult = new Remult();
const noteRepo = remult.repo(Note);

export default function Notekeeper({ data }: { data: Note[] }) {
  const [notes, setNotes] = useState<Note[]>(data);

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
    <div class="flex flex-col gap-2 pt-2 w-full">
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
          <div key={note.id}>
            {formatDate(new Date(note.timestamp))}
            <input
              value={note.note}
              onInput={(e) => handleChange({ note: e.currentTarget.value })}
            />
            <Button onClick={saveNote}>Save</Button>
            <Button onClick={deleteNote}>Delete</Button>
          </div>
        );
      })}
      <Button onClick={addNote}>Add Note</Button>
    </div>
  );
}
