import { Head } from "$fresh/runtime.ts";
import { Card } from "../components/Card.tsx";
import Debug from "../islands/Debug.tsx";
import Debug_user from "../islands/Debug_user.tsx";

export default function Home() {
	return (
		<div class="bg-gray-100 p-2">
		<Head>
				<title>Debug widget</title>
				<meta name="description" content="textarea test" />
			</Head>

			<div class=" space-y-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
				<Card>
					<Debug_user start={1} initmessage="hello" />
				</Card>
				<Card>
					<Debug start={1} initmessage="hello" />
				</Card>
				</div>
		</div>
	);
}


