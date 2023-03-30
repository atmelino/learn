import React from 'react';
import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState, useRef } from 'react';


const PeriodicTask = () => {
  const [counter, setCounter] = useState(0);
  //const [flag, setFlag] = useState(false);
  let flag = true;
  //const [counter] = useSeconds(flag);
  let count = 1;
  let interval=null;

  function startTask() {
    console.log("startTask called");
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  }

  function stopTask() {
    console.log("stopTask called")
    flag = false;
    clearInterval(interval);
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  }

  function myTask() {
    console.log("myTask called")
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
    //setCounter(count);
    count++;
    console.log("count=" + count)
    setCounter(count); 
  }

  useEffect(() => {
    interval = setInterval(myTask, 1000);
    if (!flag) {
      return () => clearInterval(interval);
    }
  }, [flag]);


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
