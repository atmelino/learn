import { INote } from "../islands/NoteKeeper.tsx";
import { Note } from "./Note.tsx";

interface TasksProps {
  tasks: INote[];
  removeNote: (s: string) => void;
}

export function Notes({ tasks, removeNote }: TasksProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {tasks?.map((task) => <Note task={task} removeNote={removeNote} />)}
    </div>
  );
}
