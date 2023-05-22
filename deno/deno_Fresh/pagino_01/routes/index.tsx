import { Head } from "$fresh/runtime.ts";
import Counter from "../islands/Counter.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>Fresh App</title>
      </Head>
      <div class="p-4 mx-auto max-w-screen-md">
        <img
          src="/logo.svg"
          class="w-32 h-32"
          alt="the fresh logo: a sliced lemon dripping with juice"
        />
        <p class="my-6">
          Welcome to `fresh`. Try updating this message in the
          ./routes/index.tsx file, and refresh ok?
        </p>
        <Counter start={3} />
      </div>
      <div>
        Examples:
        <p>
        <a href="about">about</a>
        </p>
        <p>
        <a href="testFolder/test">testFolder/test</a>
        </p>
        <p>
        <a href="greet/Luca">greet/Luca</a>
        </p>
        <p>
        <a href="github/atmelino">github/atmelino</a>
        </p>
        <p>
        <a href="search">search</a>
        </p>
        <p>
        <a href="countdown">countdown</a>
        </p>

      </div>
    </>
  );
}