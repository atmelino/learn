import React from 'react';
//import { useSeconds } from '../hooks/useSeconds';
import { useEffect, useState, useRef } from 'react';

const state = {
  timerOn: false,
  timerStart: 0,
  timerTime: 0,
  timer: null
};



const PeriodicTask = () => {
  //const { timerTime } = this.state;
  const [mytimerTime, settimerTime] = useState(state);

  const [counter, setCounter] = useState(0);
  let flag = true;
  //  const [counter] = useSeconds(flag);
  let count = 1;
  let interval = null;
  // let interval=useRef();

  function startTimer() {
    settimerTime({
      timerOn: true,
      timerTime: mytimerTime.timerTime,
      timerStart: Date.now() - mytimerTime.timerTime
    });

    mytimerTime.timer = setInterval(() => {
      console.log("startTimer called");
      console.log("myTimer=" + JSON.stringify(mytimerTime, null, 4));

      settimerTime({
        timerTime: Date.now() - mytimerTime.timerStart
      });
    }, 1000);
  };


  function stopTimer() {
    console.log("stopTimer called");
    console.log("myTimer=" + JSON.stringify(mytimerTime, null, 4));

    settimerTime({
      timerOn: false,
    });

    clearInterval(mytimerTime.timer);
  };

  function startTask() {
    console.log("startTask called");
    //interval = setInterval(myTask, 1000);

    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  }

  function stopTask() {
    console.log("stopTask called")
    flag = false;
    clearInterval(interval);
    //console.log("myTimer=" + JSON.stringify(myTimer, null, 4));
  }

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
      <div>
        <button onClick={() => startTimer()}>Start</button>
        <button onClick={() => stopTimer()}>Stop</button>
      </div>
      <p>
        counter = {counter}

      </p>
    </div>
  );

};

export default PeriodicTask;
