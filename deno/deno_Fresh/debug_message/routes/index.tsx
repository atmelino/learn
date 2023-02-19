import { Head } from "$fresh/runtime.ts";
import Debug from "../islands/Debug.tsx";
import Debug_user from "../islands/Debug_user.tsx";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Debug widget</title>
        <meta name="description" content="textarea test" />
      </Head>


      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">

      <Debug_user start={1} initmessage="hello" />
      <Debug start={1} initmessage="hello" />
      </main>
    </div>
  );
}
