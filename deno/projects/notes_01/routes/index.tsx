import { Head } from "$fresh/runtime.ts";
import HomeBody from "../islands/Home.tsx";
import { Page } from "../helper/Page.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>atmelino's Notes App</title>
      </Head>

      <Page>
        <div className="p-4 mx-auto max-w-screen-md w-full mt-10">
          <HomeBody />
          <p className="text-center text-gray-500 text-lg mt-4">
          </p>
        </div>
      </Page>
    </>
  );
}
