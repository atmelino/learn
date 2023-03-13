import { Head } from "$fresh/runtime.ts";
import { Handlers, PageProps } from "$fresh/server.ts";
import { Task } from "../model/task.ts";
import { remultServer } from "./_middleware.ts";
import Todos from "../islands/todos.tsx";

export const handler: Handlers<Task[]> = {
  async GET(req, ctx) {
    const remult = await remultServer.getRemult(req);
    return ctx.render(await remult.repo(Task).find());
  },
};

export default function Home({ data }: PageProps<Task[]>) {
  return (
    <div>
      <Head>
        <title>Notekeeper</title>
        <meta name="description" content="textarea test" />
      </Head>
      <Todos data={data} />
    </div>
  );
}