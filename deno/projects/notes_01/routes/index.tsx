import { Head } from "$fresh/runtime.ts";
import Counter from "../islands/Counter.tsx";
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
            Add a new note
          </p>
        </div>
      </Page>

      <img
        src="/logo.svg"
        class="w-32 h-32"
        alt="the fresh logo: a sliced lemon dripping with juice"
      />
      <p class="my-6">
        Welcome to `fresh`. Try updating this message in the ./routes/index.tsx
        file, and refresh.
      </p>
      <Counter start={3} />
      <div>
        <h2>Notes</h2>
      </div>
    </>
  );
}
