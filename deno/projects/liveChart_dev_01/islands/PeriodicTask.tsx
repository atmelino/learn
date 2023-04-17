import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface TaskProps {
  Task: (s: string) => void;
  name: string;
  interval: number
  autostart: boolean
  start: boolean
}

interface TaskStatus {
  id: number
  running: boolean
}


function PeriodicTask(props: TaskProps) {
  const Task = props.Task;
  const name = props.name || "default";
  const interval = props.interval || 1000;
  // const autostart = props.autostart || true;
  const autostart = props.autostart;

  // const ts1: TaskStatus =
  //   useRef({
  //     id: interval,
  //     running: false
  //   });

  const ts =
    useRef({
      id: interval,
      running: false
    });


  const [counter, setCounter] = useState(0);
  let count = 0;
  // const IntervalRef{
  //   interval: interval,
  //   running:false
  // } = useRef(0, false)
  // const intervalRef = useRef(interval);

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
    // intervalRef.current = id;
  }

  function stopTask() {
    console.log("stopTask called");
    if (ts.current.running) {
      console.log("Interval ID before setInterval=" + ts.current.id);
      clearInterval(ts.current.id);
      ts.current.running = false;
      console.log("Interval ID after setInterval=" + ts.current.id);
      // intervalRef.current = 0;
    }
    else
      console.log("Task not running");
  }

  function myTask() {
    // console.log("myTask called");
    count++;
    setCounter(count);
    Task("count=" + count);
  }

  useEffect(() => {
    console.log("useEffect in PeriodicTask");
    console.log("autostart=" + autostart);

    if (autostart)
      startTask()
  }, [props.start]);


  return (
    <div>
      <div>
        <Button onClick={() => startTask()}>Start</Button>
        <Button onClick={() => stopTask()}>Stop</Button>
        counter = {counter}
      </div>
    </div>
  );
}

export default PeriodicTask;
