import { INote } from "../islands/NoteKeeper.tsx";
import { Note } from "./Note.tsx";

interface notesProps {
  notes: INote[];
  removeNote: (s: string) => void;
}

export function Notes({ notes, removeNote }: notesProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {notes?.map((note) => <Note note={note} removeNote={removeNote} />)}
    </div>
  );
}
