import React, { Component } from "react";
import { useEffect, useState } from 'react';

//function PeriodicTask  {
export default function PeriodicTask() {
  const countDownDate = new Date(targetDate).getTime();
  const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
  const SEVEN_DAYS_IN_MS = 7 * 24 * 60 * 60 * 1000;
  const NOW_IN_MS = new Date().getTime();

  const dateTimeAfterThreeDays = NOW_IN_MS + THREE_DAYS_IN_MS;
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

