import { Head } from "$fresh/runtime.ts";
import Body from "../islands/Body.tsx";

export default function Home() {
	return (
		<div class="bg-gray-100 p-2">
			<Head>
				<title>Debug widget</title>
				<meta name="description" content="textarea test" />
			</Head>
			<Body />
		</div>
	);
}
