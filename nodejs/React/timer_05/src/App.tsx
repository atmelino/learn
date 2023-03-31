// https://blog.greenroots.info/how-to-create-a-countdown-timer-using-react-hooks

import React, { useEffect } from 'react';
import PeriodicTask from "./components/PeriodicTask";

import './App.css';

export default function App() {
  useEffect(() => {
    document.title = "timer_05";
  }, []);

  const THREE_DAYS_IN_MS = 3 * 24 * 60 * 60 * 1000;
  const SEVEN_DAYS_IN_MS = 7 * 24 * 60 * 60 * 1000;
  const NOW_IN_MS = new Date().getTime();

  const dateTimeAfterSevenDays = NOW_IN_MS + SEVEN_DAYS_IN_MS;

  return (
    <div>

      <PeriodicTask  />

    </div>
  );
}
