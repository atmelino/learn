import React, { Component } from "react";
//import { Helmet } from 'react-helmet';
import Helmet from 'react-helmet';

import Stopwatch from "./components/Stopwatch";
import Countdown from "./components/Countdown";

class App extends Component {
  render() {
    return (
      
      <div className="App">
        <Helmet>
          <title>timer_04</title>
        </Helmet>
        <div className="App-title">Timers Demo</div>
        <div className="Timers">
          <Stopwatch />
          <Countdown />
        </div>
      </div>
    );
  }
}

export default App;