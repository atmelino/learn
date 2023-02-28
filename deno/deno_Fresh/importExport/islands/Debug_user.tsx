import { ButtonGreen } from "../components/ButtonGreen.tsx";
import * as mydebug from "../islands/Debug.tsx";

interface debugProps {
	start: number;
	initmessage: string;
}

export default function Debug_user(props: debugProps) {
	function setDebugText(message: string) {
		console.log("button pressed");
		mydebug.setMyGlobalString(message);
		mydebug.myGlobalFunction();
	}

	return (
		<div class="w-full pt-5">
			<h2 class="text-lg font-medium text-gray-900 ">Debug User</h2>
			This element uses the debug element by sending a message to it

			<div class="flex gap-2 w-full">
				<ButtonGreen
					className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-1/2"
					onClick={() => setDebugText("text from debug user")}
				>
					send debug message
				</ButtonGreen>
			</div>
		</div>
	);
}
