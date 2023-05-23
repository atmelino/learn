import { useEffect, useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import Pagino from './Pagino.tsx';

export default function Body() {
  const count = useRef(0);

  useEffect(() => {
    count.current = count.current + 1;
  });

  function onChange() { }

  return (
    <div class="flex flex-row justify-evenly">
      <Pagino
        count={10}
        showFirst={true}
        showPrevious={true}
        showNext={true}
        showLast={true}
        page={1}
        siblingCount={1}
        boundaryCount={1}
        onChange={onChange}
      />
    </div>
  );
}
