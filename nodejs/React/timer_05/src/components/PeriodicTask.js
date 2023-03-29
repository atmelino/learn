import React from 'react';
import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState } from 'react';


const PeriodicTask = ({ targetDate }) => {
  const [days, hours, minutes, seconds] = useSeconds(targetDate);
  const [counter, setCounter] = useState(0);
  //const [myTimer, setmyTimer] = useState(null);


  function startTask() {
    console.log("startTask called")
    setInterval(myTask, 2000);
    //setCounter(counter => counter + 1);
  }

  function myTask() {
    console.log("myTask called")
    console.log("counter=" + counter)
    //let tmpvar = counter + 1;
    setCounter(15);
  }



  return (
    <div>
      seconds = {seconds}

      <button onClick={() => startTask()}>Start</button>
      {counter}

    </div>
  );

};

export default PeriodicTask;
