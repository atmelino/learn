import { useState } from "preact/hooks";
import { format } from "https://deno.land/std@0.91.0/datetime/mod.ts";
import { Button } from "../components/Button.tsx";
import { Chart } from "$fresh_charts/mod.ts";
import { months, numbers } from "../utils.ts";

export interface DebugProps {
  mynumbers: typeof numbers;
  setmynumbers: (s: typeof numbers) => void;
}

//export default function MyIsland({ mynumbers, setmynumbers }: DebugProps) {
export default function MyIsland() {
  const barCfg = { count: 7, min: -100, max: 100 };
  const [mynumbers, setmynumbers] = useState(numbers(barCfg));
  //let mynumbers = numbers(barCfg);

  const addNote = () => {
    console.log("addNote called");
    setmynumbers(numbers(barCfg));
    //mynumbers = numbers(barCfg);
  };

  return (
    <div class="p-4 mx-auto max-w-screen-md">
      <Button onClick={addNote}>Add Note</Button>
      <div>{mynumbers}</div>
    </div>
  );
}
