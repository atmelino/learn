/** @jsx h */
import { h } from "preact";
import { Handlers, PageProps } from "$fresh/server.ts";
import Notekeeper from "../islands/notekeeper.tsx";
import { Note } from "../model/note.ts";
import { remultServer } from "./_middleware.ts";
import { Head } from "$fresh/runtime.ts";

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
        <title>Remult with conf object</title>
        <meta name="description" content="textarea test" />
      </Head>
      <Notekeeper data={data} />
    </div>
  );
}
