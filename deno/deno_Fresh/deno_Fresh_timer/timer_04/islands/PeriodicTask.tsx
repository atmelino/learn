import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

interface TaskProps {
  TaskName: (s: string) => void;
	name: string;
}

function PeriodicTask({ TaskName }: TaskProps) {
  const [counter, setCounter] = useState(0);
  let count = 0;
  const intervalRef = useRef(2000);

  function startTask() {
    console.log("startTimer called");
    const id = setInterval(myTask, 1000);
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
    TaskName("count="+count);
  }

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
