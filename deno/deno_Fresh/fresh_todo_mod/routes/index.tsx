import { Head } from "$fresh/runtime.ts";
import Debug from "../islands/Debug.tsx";
import NoteKeeper from "../islands/NoteKeeper.tsx";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Fresh NoteKeeper</title>
        <meta name="description" content="Fresh NoteKeeper" />
      </Head>
      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
        <NoteKeeper />
        <Debug initmessage="hello" />
      </main>
    </div>
  );
}
