import { Head } from "$fresh/runtime.ts";
import PeriodicTask from "../islands/PeriodicTask.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>timer_01</title>
      </Head>
      <div class="p-4 mx-auto max-w-screen-md">
        <PeriodicTask />
      </div>
    </>
  );
}
