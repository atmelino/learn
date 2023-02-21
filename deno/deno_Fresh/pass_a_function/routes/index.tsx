import { Head } from "$fresh/runtime.ts";
import Body from "../islands/Body.tsx";
import Debug from "../islands/Debug.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>deno popup demo</title>
      </Head>

      <Body />
    </>
  );
}
