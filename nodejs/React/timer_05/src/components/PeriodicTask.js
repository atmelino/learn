import React from 'react';
import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState, useRef  } from 'react';


const PeriodicTask = ({ targetDate }) => {
  const [days, hours, minutes, seconds] = useSeconds(targetDate);
  const [counter, setCounter] = useState(0);
  //const [myTimer, setmyTimer] = useState(0);
  let myTimer = useRef();

  let count = 1;
  //let myTimer = setInterval(myTask, 2000);
  //clearInterval(myTimer);

  function startTask() {
    console.log("startTask called");
    myTimer=setInterval(myTask, 2000);
    console.log(JSON.stringify(myTimer, null, 4));
    //console.log("myTimer="+myTimer);
  }

  function stopTask() {
    console.log("stopTask called")
    clearInterval(myTimer);
    console.log(JSON.stringify(myTimer, null, 4));
  }

  function myTask() {
    console.log("myTask called")
    //console.log("counter=" + counter)
    //let tmpvar = counter + 1;
    setCounter(count);
    count++;
    console.log("count=" + count)
  }



  return (
    <div>
      seconds = {seconds}

      <button onClick={() => startTask()}>Start</button>
      <button onClick={() => stopTask()}>Stop</button>
      {counter}

    </div>
  );

};

export default PeriodicTask;
