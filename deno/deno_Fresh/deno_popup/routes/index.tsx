import { Head } from "$fresh/runtime.ts";
import { Header } from "../components/Header.tsx";
import IconSettings from "../components/IconSettings.tsx";

export default function Home() {
  return (
    <>
      <Head>
        <title>deno popup demo</title>
      </Head>
      <Header />
      <div>
        Click on the settings icon to open the popup window
      </div>
      <IconSettings size={20} />

    </>
  );
}
