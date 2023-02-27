import { JSX } from "preact";
import { IS_BROWSER } from "$fresh/runtime.ts";

export function Card(props: JSX.HTMLAttributes<HTMLDivElement>) {
  return (
    <div
      {...props}
      disabled={!IS_BROWSER || props.disabled}
      class="block max-w-sm rounded-lg bg-white p-6 shadow-lg "
    />
  );
}
//      class="py-8 px-6 h-full bg-white ${corners} flex flex-col justify-between hover:bg-gray-200"
