import React from "react";
import { useEffect, useRef, useState } from "react";

type ButtonProps = {
  onClick(): void;
  name: string;
  children: React.ReactNode;
};

const PeriodicTask2: React.FunctionComponent<ButtonProps> = (
  { children, ...props },
) => {
  const [counter, setCounter] = useState(0);
  let count = 1;
  const intervalRef: { current: NodeJS.Timeout | null } = useRef(null);

  const { onClick, name } = props;
  function startTask() {
    console.log("startTimer called");
    const id = setInterval(myTask, 1000);
    intervalRef.current = id;
  }

  function stopTask() {
    console.log("stopTimer called");
    clearInterval(intervalRef.current as NodeJS.Timeout);
  }

  function myTask() {
    console.log("myTask called");
    count++;
    setCounter(count);
    onClick();

  }

  return (
    <div>
      <button onClick={onClick}>{children}</button>
      <div>
        <button onClick={() => startTask()}>Start</button>
        <button onClick={() => stopTask()}>Stop</button>
      </div>
    </div>
  );
};

export default PeriodicTask2;
