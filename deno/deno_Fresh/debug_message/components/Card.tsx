import { JSX } from "preact";
import { IS_BROWSER } from "$fresh/runtime.ts";

export function Card(props: JSX.HTMLAttributes<HTMLDivElement>) {
  const corners = "rounded(tl-2xl tr-2xl sm:(tr-none bl-2xl))";
	const card = `p-2 py-5 h-full bg-white ${corners}  justify-between`;

  return (
    <div
      {...props}
      disabled={!IS_BROWSER || props.disabled}
      class={card}
      />
  );
}
//      class="py-8 px-6 h-full bg-white ${corners} flex flex-col justify-between hover:bg-gray-200"
