import React, { useEffect, useMemo, useState } from 'react';
import './App.css';
import Pagino from "./pagino";

function App() {
  const [pages, setPages] = useState([]);

  const pagino = useMemo(() => {
    const _ = new Pagino({
      onChange: (page, count) => {
        setPages(_.getPages());
        // console.log("calling setPages")
      }
    });

    _.setCount(10);

    return _;
  }, []);

  const handlePaginoNavigation = (type) => {
    console.log("enter handlePaginoNavigation()")
    console.log(
      "this.bC_c_p_sC",
      pagino.boundaryCount,
      pagino.count,
      pagino.page,
      pagino.siblingCount,
    );

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
        onClick={() => handlePaginoNavigation(page)}
      >
        {page}
      </button>
    );
  };

  useEffect(() => {
    document.title = "pagino_01 React";
  }, []);


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
