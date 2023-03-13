import { Remult } from "remult";
import { useState } from "preact/hooks";
import { Task } from "../model/task.ts";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";

const remult = new Remult();
const taskRepo = remult.repo(Task);

export default function Todos({ data }: { data: Task[] }) {
  const [tasks, setTasks] = useState<Task[]>(data);

  const addTask = () => {
    setTasks([...tasks, new Task()]);
  };


  function getDate() {
    const date_ob = new Date();
    console.log(format(date_ob, "yyyy-MM-dd HH:mm:ss"));
    const timestamp = format(date_ob, "yyyy-MM-dd HH:mm:ss");
    return timestamp;
  }

  return (
    <div>
      {tasks.map((task) => {
        const handleChange = (values: Partial<Task>) => {
          setTasks(tasks.map((t) => t === task ? { ...task, ...values } : t));
        };

        const saveTask = async () => {
          const savedTask = await taskRepo.save(task);
          setTasks(tasks.map((t) => t === task ? savedTask : t));
        };

        const deleteTask = async () => {
          await taskRepo.delete(task);
          setTasks(tasks.filter((t) => t !== task));
        };

        return (
          <div key={task.id}>
            Date:{task.timestamp}
            <input
              value={task.note}
              //onInput={(e) => handleChange({ note: e.currentTarget.value, timestamp:getDate() })}
              onInput={(e) =>
                handleChange({
                  note: e.currentTarget.value,
                  timestamp: new Date(),
                })}
              // onInput={(e) => handleChange({ note: e.currentTarget.value })}
            />
            <button onClick={saveTask}>Save</button>
            <button onClick={deleteTask}>Delete</button>
          </div>
        );
      })}
      <button onClick={addTask}>Add Task</button>
    </div>
  );
}
