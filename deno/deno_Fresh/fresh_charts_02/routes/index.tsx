import { Head } from "$fresh/runtime.ts";
import Counter from "../islands/Counter.tsx";
import MyChart from "./MyChart.tsx";
import MyIsland from "../islands/MyIsland.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>Fresh App</title>
      </Head>

      <div>
        <MyIsland />
      </div>

      <div class="p-4 mx-auto max-w-screen-md">
        <MyChart />
      </div>

    </>
  );
}
