// routes/greet/[name].tsx

import { PageProps } from "$fresh/server.ts";

export default function GreetPage(props: PageProps) {
  const { name } = props.params;
  const name2  = props.url.pathname;
  return (
    <main>
      <p>Greetings to you, {name}!</p>
      <p>URL is {name2}!</p>
    </main>
  );
}1

