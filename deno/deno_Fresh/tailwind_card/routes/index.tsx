import { Head } from "$fresh/runtime.ts";
import { Card } from "../components/Card.tsx";
import Content from "../islands/Content.tsx";
import Content2 from "../islands/Content2.tsx";

export default function Home() {
  return (
    <div class="bg-gray-100 p-2">
      <Head>
        <title>Fresh App</title>
      </Head>

      <div class=" space-y-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
        <Card>
          <Content />
        </Card>
        <Card>
          <Content2 />
        </Card>
      </div>
    </div>
  );
}
