import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";

const PeriodicTask = () => {
  const [counter, setCounter] = useState(0);
  let count = 1;
  const intervalRef = useRef(2000);

  function startTask() {
    console.log("startTimer called");
    const id = setInterval(() => {
      console.log("Timer function called");
      count++;
      setCounter(count);
    }, 1000);
    intervalRef.current = id;
  }

  function stopTask() {
    console.log("stopTimer called");
    clearInterval(intervalRef.current);
  }

  return (
    <div>
      <div>
        <Button onClick={() => startTask()}>Start</Button>
        <Button onClick={() => stopTask()}>Stop</Button>
      </div>
      <p>
        counter = {counter}
      </p>
    </div>
  );
};

export default PeriodicTask;
