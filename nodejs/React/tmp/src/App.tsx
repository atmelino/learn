import React from "react";
import logo from "./logo.svg";
import "./App.css";
import PeriodicTask from "./components/PeriodicTask";
import Helmet from "react-helmet";

function App() {
  return (
    <div className="App">
      <Helmet>
        <title>timer_05</title>
      </Helmet>
      <header className="App-header">
      </header>
      <PeriodicTask />
    </div>
  );
}

export default App;
