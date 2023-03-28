// https://blog.openreplay.com/build-a-react-timer-application-with-useref

import React, { useState, useRef } from 'react';

import './App.css';
  
  
function App() {
  const [insert, setInsert] = useState('');
  const [secs, setSecs] = useState(0);
  const reference = useRef(0);
  const time = useRef();
  
  const handleOnchange = (e) => {
    setInsert(e.target.value);
    reference.current++;
  }
  
  const startTime = () => {
    time.current = setInterval(() => {
      reference.current++;
      setSecs(prev => prev + 1)
    }, 1000)
  }
  
  const stopTime = () => {
    clearInterval(time.current);
    time.current = 0;
  }
  
  const resetTime = () => {
    stopTime();
    if (secs) {
      reference.current++;
      setSecs(0);
    }
  }
  return (
    <div className='App'>
      <input
        type="text"
        placeholder='use reference'
        value={insert}
        onChange={handleOnchange}
        className="input"
      />
      <br /><br />
      <div className='text'> <p className='text'>Please input your name: {insert}</p></div>
      <div >
      </div>
      <input type="button" value="start time" onClick={startTime} />
      <input type="button" value="stop time" onClick={stopTime} />
      <input type="button" value="reset time" onClick={resetTime} />
      <p>Timer{secs}</p>
      <div>
        <p>Render:[{reference.current}]</p>
      </div>
    </div>
  );
}
  
export default App;