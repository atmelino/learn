import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface TaskProps {
  Task: (s: string) => void;
  name: string;
  interval: number
  autostart: true
}
function PeriodicTask(props: TaskProps) {
  const Task = props.Task;
  const name = props.name || "default";
  const interval = props.interval || 1000;
  const autostart = props.autostart || true;


  const [counter, setCounter] = useState(0);
  let count = 0;
  const intervalRef = useRef(interval);

  function startTask() {
    console.log("startTimer called");
    const id = setInterval(myTask, interval);
    intervalRef.current = id;
  }

  function stopTask() {
    console.log("stopTimer called");
    clearInterval(intervalRef.current);
  }

  function myTask() {
    // console.log("myTask called");
    count++;
    setCounter(count);
    Task("count=" + count);
  }

  useEffect(() => {
    if (autostart)
      startTask()
  }, []);


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
