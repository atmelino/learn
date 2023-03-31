import { useEffect, useState } from "react";

const useSeconds = (flag) => {
  const [counter, setCounter] = useState(0);
  let count = 1;

  useEffect(() => {
    console.log("useEffect called");

    const interval = setInterval(() => {
      count++;
      setCounter(count);
    }, 1000);
    return () => {
      console.log("clearInterval in useEffect called");
      clearInterval(interval);
    };
  }, [count]);

  return [counter];
};

export { useSeconds };
