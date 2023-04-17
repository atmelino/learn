import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface TaskProps {
  Task: (s: string) => void;
  name: string;
  interval: number
  start: boolean
}

function PeriodicTask(props: TaskProps) {
  const Task = props.Task;
  const name = props.name || "default";
  const interval = props.interval || 1000;
  const start = props.start;
  const ts =
    useRef({
      id: interval,
      running: false
    });

  const count = useRef(0);

  function startTask() {
    console.log("startTask called");
    if (!ts.current.running) {
      console.log("Interval ID before setInterval=" + ts.current.id);
      const id = setInterval(myTask, interval);
      ts.current.id = id;
      ts.current.running = true
      console.log("Interval ID after setInterval=" + ts.current.id);
    } else
      console.log("Task already running");
  }

  function stopTask() {
    console.log("stopTask called");
    if (ts.current.running) {
      console.log("Interval ID before setInterval=" + ts.current.id);
      clearInterval(ts.current.id);
      ts.current.running = false;
      console.log("Interval ID after setInterval=" + ts.current.id);
    }
    else
      console.log("Task not running");
  }

  function myTask() {
    // console.log("myTask called");
    count.current++;
    Task("count=" + count);
  }

  useEffect(() => {
    console.log("useEffect in PeriodicTask");
    console.log("start=" + start);

    if (start)
      startTask()
  }, [props.start]);


  return (
    <div>
      <div>
        <Button onClick={() => startTask()}>Start</Button>
        <Button onClick={() => stopTask()}>Stop</Button>
        counter =  {count.current}
      </div>
    </div>
  );
}

export default PeriodicTask;
