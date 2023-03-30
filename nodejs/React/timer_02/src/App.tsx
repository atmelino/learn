// https://blog.greenroots.info/how-to-create-a-countdown-timer-using-react-hooks

import React, { useEffect } from "react";
import CountdownTimer from "./CountdownTimer.js";
import "./App.css";

export default function App() {
  useEffect(() => {
    document.title = "timer_02";
  }, []);

  const SEVEN_DAYS_IN_MS = 7 * 24 * 60 * 60 * 1000;
  const TEN_SECONDS_IN_MS = 10 * 1000;
  const NOW_IN_MS = new Date().getTime();

  const dateTimeAfterSevenDays = NOW_IN_MS + SEVEN_DAYS_IN_MS;
  const dateTimeAfterTenSeconds = NOW_IN_MS + TEN_SECONDS_IN_MS;

  return (
    <div>
      <h1>Countdown Timer</h1>

      <h2>Expires after 7 days:</h2>
      <CountdownTimer targetDate={dateTimeAfterSevenDays} />

      <h2>Expires after 10 seconds:</h2>
      <CountdownTimer targetDate={dateTimeAfterTenSeconds} />

    </div>
  );
}
