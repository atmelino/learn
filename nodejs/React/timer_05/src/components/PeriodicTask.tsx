import React from "react";
import { useEffect, useRef, useState } from "react";

const PeriodicTask = () => {
  const [counter, setCounter] = useState(0);
  let count = 1;
  const intervalRef: { current: NodeJS.Timeout | null } = useRef(null);

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

    clearInterval(intervalRef.current as NodeJS.Timeout);
  }

  return (
    <div>
      <div>
        <button onClick={() => startTask()}>Start</button>
        <button onClick={() => stopTask()}>Stop</button>
      </div>
      <p>
        counter = {counter}
      </p>
    </div>
  );
};

export default PeriodicTask;
