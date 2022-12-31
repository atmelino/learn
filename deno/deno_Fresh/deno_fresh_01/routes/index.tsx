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
        <a href="http://localhost:8000/about">http://localhost:8000/about</a>
        </p>
        <p>
        <a href="http://localhost:8000/testFolder/test">http://localhost:8000/testFolder/test</a>
        </p>
        <p>
        <a href="http://localhost:8000/greet/Luca">http://localhost:8000/greet/Luca</a>
        </p>
        <p>
        <a href="http://localhost:8000/github/atmelino">http://localhost:8000/github/atmelino</a>
        </p>
        <p>
        <a href="http://localhost:8000/search">http://localhost:8000/search</a>
        </p>
        <p>
        <a href="http://localhost:8000/countdown">http://localhost:8000/countdown</a>
        </p>
        <p>
        <a href="http://localhost:8000/showIP">http://localhost:8000/showIP</a>
        </p>

      </div>
    </>
  );
}
