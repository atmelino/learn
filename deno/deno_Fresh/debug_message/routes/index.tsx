import { Head } from "$fresh/runtime.ts";
import Debug from "../islands/Debug.tsx";
import Debug_user from "../islands/Debug_user.tsx";

export default function Home() {
  const corners = "rounded(tl-2xl tr-2xl sm:(tr-none bl-2xl))";
  const card =
    `py-8 px-6 h-full bg-white ${corners} flex flex-col justify-between`;
  return (
    <div>
      <Head>
        <title>Debug widget</title>
        <meta name="description" content="textarea test" />
      </Head>

      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
        <Debug_user start={1} initmessage="hello" />

        <div>
          <div class={card}>
            <div class="border-t border-gray-200 py-6 px-4 sm:px-6">
              <div class="flex justify-between text-lg font-medium">
                <p>A Number:</p>
              </div>
            </div>
          </div>
        </div>

        <Debug start={1} initmessage="hello" />
      </main>
    </div>
  );
}
