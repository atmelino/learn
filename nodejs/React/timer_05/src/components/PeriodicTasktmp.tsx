import React from "react";
//import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useRef, useState } from "react";

const state = {
  timerOn: false,
  timerStart: 0,
  timerTime: 0,
  timer: null,
};

const PeriodicTask = () => {
  //const { timerTime } = this.state;
  const [mytimerTime, settimerTime] = useState(state);
  const [counter, setCounter] = useState(0);
  const [prevFlipping, setIsFlipping] = useState(true);
  //  const [counter] = useSeconds(flag);
  let count = 1;
  //  let interval = null;
  // let interval=useRef();
  const intervalRef: { current: NodeJS.Timeout | null } = useRef(null);

  function startTask() {
    console.log("startTimer called");

    const id = setInterval(() => {
      count++;
      setCounter(count);
      setIsFlipping((prevFlipping) => !prevFlipping);
    }, 10000);
    intervalRef.current = id;
  }

  function stopTask() {
    console.log("stopTimer called");

    clearInterval(intervalRef.current as NodeJS.Timeout);
  }

  // function startTimer() {
  //   settimerTime({
  //     timerOn: true,
  //     timerTime: mytimerTime.timerTime,
  //     timerStart: Date.now() - mytimerTime.timerTime,
  //   });

  //   mytimerTime.timer = setInterval(() => {
  //     console.log("startTimer called");
  //     console.log("myTimer=" + JSON.stringify(mytimerTime, null, 4));

  //     settimerTime({
  //       timerTime: Date.now() - mytimerTime.timerStart,
  //     });
  //   }, 1000);
  // }

  // function stopTimer() {
  //   console.log("stopTimer called");
  //   console.log("myTimer=" + JSON.stringify(mytimerTime, null, 4));

  //   settimerTime({
  //     timerOn: false,
  //   });

  //   clearInterval(mytimerTime.timer);
  // }

  // function startTask() {
  //   console.log("startTask called");
  //   //interval = setInterval(myTask, 1000);

    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  // }

  // function stopTask() {
  //   console.log("stopTask called");
  //   //flag = false;
    //clearInterval(interval);
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  // }

  // function myTask() {
  //   console.log("myTask called")
  //   //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  //   //setCounter(count);
  //   count++;
  //   console.log("count=" + count)
  //   setCounter(count);
  // }

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
