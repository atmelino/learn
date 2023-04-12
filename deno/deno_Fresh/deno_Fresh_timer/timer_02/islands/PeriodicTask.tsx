import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";


interface TaskProps {
  length: number;
  Url: string;
  //functionToCall: (s: string) => void;
  TaskName: () => void;
}

function PeriodicTask({ length, Url, TaskName }: TaskProps) {
  const [counter, setCounter] = useState(0);
  let count = 1;
  const intervalRef = useRef(2000);

  // const { TaskName, name } = ;

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
    console.log("myTask called");
    count++;
    setCounter(count);
    TaskName();
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
