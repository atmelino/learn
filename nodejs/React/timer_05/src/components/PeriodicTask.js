import React from 'react';
import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState } from 'react';


const PeriodicTask = ({ targetDate }) => {
  const [days, hours, minutes, seconds] = useSeconds(targetDate);
  const [counter, setCounter] = useState(0);


  function startTask() {
    console.log("startTask called")
    setInterval(myTask, 3000);
    setCounter(counter + 1);
  }

  function myTask() {
    console.log("myTask called")
    setCounter(counter + 1);
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
