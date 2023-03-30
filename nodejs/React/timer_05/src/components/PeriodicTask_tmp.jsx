import React from 'react';
import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState, useRef } from 'react';


const PeriodicTask = ({ targetDate }) => {
  const [ seconds] = useSeconds(targetDate);
  const [counter, setCounter] = useState(0);
  //const [myTimer, setmyTimer] = useState(0);
  //  let myTimer = useRef();

  let count = 1;
  let myTimer = setInterval(myTask, 2000);
  clearInterval(myTimer);

  function startTask() {
    console.log("startTask called");
    myTimer = setInterval(myTask, 2000);
    console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
    //console.log("myTimer="+myTimer);
  }

  function stopTask() {
    console.log("stopTask called")
    console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
    clearInterval(myTimer);
  }

  function myTask() {
    console.log("myTask called")
    console.log("myTimer=" + JSON.stringify(myTimer, null, 4));

    //console.log("counter=" + counter)
    //let tmpvar = counter + 1;
    setCounter(count);
    count++;
    console.log("count=" + count)
  }



  return (
    <div>
      <div>
        <button onClick={() => startTask()}>Start</button>
        <button onClick={() => stopTask()}>Stop</button>
        {counter}
      </div>
      <p>
        seconds = {seconds}

      </p>
    </div>
  );

};

export default PeriodicTask;
