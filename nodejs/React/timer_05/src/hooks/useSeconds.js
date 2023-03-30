import { useEffect, useState } from "react";

const useSeconds = (flag) => {
  const [counter, setCounter] = useState(0);
  let count = 1;

  useEffect(() => {
    const interval = setInterval(() => {
      count++;
      setCounter(count);
    }, 1000);

    //return () => clearInterval(interval);
  }, [flag]);

  return [counter];
};

export { useSeconds };
