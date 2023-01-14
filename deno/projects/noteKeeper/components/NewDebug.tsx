import { Button } from "../components/Button.tsx";

interface debugProps {
  debug: string;
}

export function NewDebug({ debug }: debugProps) {
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

