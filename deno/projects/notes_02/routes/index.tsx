import { Head } from "$fresh/runtime.ts";
import NotesPage from "../islands/NotesPage.tsx";

export default function Home() {
  return (
    <div>
      <Head>
      <title>atmelino's Notes App</title>
        <meta name="description" content="Fresh Notes List" />
      </Head>
      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
        <h1 class="text-3xl p-2">
          Notes App
        </h1>
        <NotesPage />
      </main>
    </div>
  );
}
