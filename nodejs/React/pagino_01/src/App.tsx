import React, { useMemo, useState } from 'react';
import './App.css';
import Pagino from "pagino";

function App() {
  const [pages, setPages] = useState([]);

  const pagino = useMemo(() => {
    const _ = new Pagino({
      onChange: (page, count) => setPages(_.getPages())
    });

    _.setCount(10);

    return _;
  }, []);

  const hanglePaginoNavigation = (type) => {
    if (typeof type === "string") {
      pagino[type]?.();
      return;
    }

    pagino.setPage(type);
  };

  const renderElement = (page) => {
    if (page === "start-ellipsis" || page === "end-ellipsis") {
      return <button key={page}>...</button>;
    }

    return (
      <button
        style={{
          backgroundColor: page === pagino.page ? "#0971f1" : ""
        }}
        key={page}
        onClick={() => hanglePaginoNavigation(page)}
      >
        {page}
      </button>
    );
  };



  return (
    <div className="App">
      Learn React
      <div>
        <h1>Page: {pagino.page}</h1>
        <ul>{pages.map(renderElement)}</ul>
      </div>

    </div>

  );
}

export default App;
