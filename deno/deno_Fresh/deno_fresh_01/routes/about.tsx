// routes/about.tsx

import { Handlers } from "$fresh/server.ts";

export const handler: Handlers = {
  async GET(req, ctx) {
    const resp = await ctx.render();
    resp.headers.set("X-Custom-Header", "Hello");
    console.log("handler in about.tsx called");

    return resp;
  },
};


export default function AboutPage() {
  return (
    <main>
      <h1>About</h1>
      <p>This is the about page.<br></br>
        Date: 12/28/2022
      </p>
      <p>
        <a href="/">Home</a>
        </p>
    </main>
  );
}