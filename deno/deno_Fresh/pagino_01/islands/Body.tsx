import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import Pagino from './Pagino.tsx';

export default function Body() {
  const count = useRef(0);


  // const pagino = new Pagino();
  // pagino.setCount(10);
  // pagino.setPage(1);
  // pagino.getPages();


  useEffect(() => {
    count.current = count.current + 1;
  });

  function onChange() { }
  
  return (
    <div class="flex flex-row justify-evenly">
    <Pagino
        showFirst={true}
        showPrevious={true}
        showNext={true}
        showLast={true}
        page={1}
        count={8}
        siblingCount={1}
        boundaryCount={1}
        onChange={onChange}
      />
    </div>
  );
}
