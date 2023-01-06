import { INote} from "../islands/NotesPage.tsx";
import { Note } from "./Note.tsx";

interface NotesProps {
  notes: INote[];
  removeNote: (s: string) => void;
}

export function Notes({ notes, removeNote }: NotesProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {notes?.map((note) => <Note note={note} removeNote={removeNote} />)}
    </div>
  );
}
