import { useRef, useState } from "preact/hooks";
import { Button } from "../components/Button.tsx";
import { Client } from "https://deno.land/x/mysql@v2.11.0/mod.ts";
import settings from "../../../../../settings.js";

interface debugProps {
  debug: string;
}

export function Debug2({ debug }: debugProps) {
  const [dbread, setdbRead] = useState("database");

  return (
    <div class="flex flex-col gap-2 pt-2 w-full">
      {
        <div>
          <textarea
            class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
          >
            {debug}
          </textarea>
        </div>
      }
    </div>
  );
}

