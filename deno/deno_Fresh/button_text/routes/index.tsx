import { Head } from "$fresh/runtime.ts";
import Debug from "../islands/Debug.tsx";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Debug Panel</title>
        <meta name="description" content="Fresh Debug Panel" />
      </Head>
      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
        <Debug start={1} initmessage="hello" />
      </main>
    </div>
  );
}
