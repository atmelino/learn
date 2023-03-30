import React from 'react';
import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState, useRef } from 'react';


const PeriodicTask = ({ flag }) => {
  const [counter] = useSeconds(flag);
  //const [counter, setCounter] = useState(0);
  const [taskOnOff, settaskOnOff] = useState(false);

  let count = 1;

  function startTask() {
    console.log("startTask called");
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  }

  function stopTask() {
    console.log("stopTask called")
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  }

  function myTask() {
    console.log("myTask called")
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
    //setCounter(count);
    count++;
    console.log("count=" + count)
  }

  // useEffect(() => {
  //   const interval = setInterval(() => {
  //     setCountDown(countDownDate - new Date().getTime());
  //   }, 1000);

  //   return () => clearInterval(interval);
  // }, [countDownDate]);

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
