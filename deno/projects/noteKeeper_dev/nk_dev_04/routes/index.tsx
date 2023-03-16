

import { Head } from "$fresh/runtime.ts";
import { Handlers, PageProps } from "$fresh/server.ts";
import Notekeeper from "../islands/notekeeper.tsx";
import { Note } from "../model/note.ts";
import { remultServer } from "./_middleware.ts";

export const handler: Handlers<Note[]> = {
  async GET(req, ctx) {
    const remult = await remultServer.getRemult(req);
    return ctx.render(await remult.repo(Note).find());
  },
};

export default function Home({ data }: PageProps<Note[]>) {
  return (
    <div>
      <Head>
        <title>Notekeeper</title>
        <meta name="description" content="textarea test" />
      </Head>

      <main class="p-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
      <Notekeeper data={data} />
      </main>

    </div>
  );
}
