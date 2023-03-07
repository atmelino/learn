/** @jsx h */
import { h } from "preact";
import { Handlers, PageProps } from "$fresh/server.ts";
import Todos from "../islands/todos.tsx";
import { Task } from "../model/task.ts";
import { remultServer } from "./_middleware.ts";

export const handler: Handlers<Task[]> = {
  async GET(req, ctx) {
    console.log("handler in index.tsx")
    const remult = await remultServer.getRemult(req);
    return ctx.render(await remult.repo(Task).find());
  },
};

export default function Home({ data }: PageProps<Task[]>) {
  console.log("Home in index.tsx")

  return (
    <div>
      <Todos data={data} />
    </div>
  );
}