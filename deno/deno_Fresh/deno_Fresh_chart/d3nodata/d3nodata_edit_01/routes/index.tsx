import { Head } from "$fresh/runtime.ts";
import MyBarChart from "../iss/MyBarChart.tsx";
import MyLineChart from "../islands/MyLineChart.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>d3nodata_edit_04</title>
      </Head>
      <div class="p-4 mx-auto max-w-screen-md">
      </div>
      {/* <MyBarChart></MyBarChart> */}
      <MyLineChart></MyLineChart>
    </>
  );
}
