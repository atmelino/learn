import { INote } from "../islands/NoteKeeper.tsx";
import { Task } from "./Task.tsx";

interface TasksProps {
  tasks: INote[];
  removeNote: (s: string) => void;
}

export function Tasks({ tasks, removeNote }: TasksProps) {
  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {tasks?.map((task) => <Task task={task} removeNote={removeNote} />)}
    </div>
  );
}
