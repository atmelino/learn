import React, { useEffect } from "react";
import PeriodicTask from "./components/PeriodicTask";

import logo from "./logo.svg";
import "./App.css";

function App() {
  useEffect(() => {
    document.title = "timer_05";
  }, []);

  return (
    <div className="App">
      <div>
        <PeriodicTask />
      </div>
    </div>
  );
}

export default App;
