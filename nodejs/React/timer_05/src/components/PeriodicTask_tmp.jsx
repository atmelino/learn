import React, { Component } from "react";
import { useEffect, useState } from 'react';

//function PeriodicTask  {
export default function PeriodicTask() {
 

  const targetDate = dateTimeAfterThreeDays;
  //  render() {
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

  const [countDown, setCountDown] = useState(
    countDownDate - new Date().getTime()
  );

  useEffect(() => {
    const interval = setInterval(() => {
      setCountDown(countDownDate - new Date().getTime());
    }, 1000);

    return () => clearInterval(interval);
  }, [countDownDate]);

  // setCounter = () => {

  // }
  return (
    <div>
      <p>
        hello
      </p>
      <button onClick={() => startTask()}>Start</button>
      {counter}
    </div>
  );
}

//}

