import React, { useMemo, useState } from 'react';
import './App.css';
import Pagino from "./pagino";

function App() {
  const [pages, setPages] = useState([]);

  const pagino = useMemo(() => {
    const _ = new Pagino({
      onChange: (page, count) => setPages(_.getPages())
    });

    _.setCount(10);

    return _;
  }, []);





