import { Head } from "$fresh/runtime.ts";
import Todo from "../islands/Todo.tsx";
import Debug from "../islands/Debug.tsx";

export default function Home() {
  return (
    <div>
      <Head>
        <title>Fresh ToDo List</title>
        <meta name="description" content="Fresh ToDo List" />
      </Head>
      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
        <Todo />
        <Debug initmessage="hello" />
      </main>
    </div>
  );
}
