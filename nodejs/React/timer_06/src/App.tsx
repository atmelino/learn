// https://blog.greenroots.info/how-to-create-a-countdown-timer-using-react-hooks

import React, { useEffect } from 'react';
import PeriodicTask from "./components/PeriodicTask";

import './App.css';

export default function App() {
  useEffect(() => {
    document.title = "timer_06";
  }, []);

  return (
    <div>

      <PeriodicTask  />

    </div>
  );
}
