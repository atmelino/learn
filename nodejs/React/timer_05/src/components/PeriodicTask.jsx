import React, { Component } from "react";
import { useEffect, useState } from 'react';

//function PeriodicTask  {
export default function PeriodicTask() {


  //  render() {
  const [counter, setCounter] = useState(0);
  function startTask ()  {
    setCounter(counter + 1);
  }

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

