import { useRef, useState } from "preact/hooks";
import { ButtonGreen } from "../components/ButtonGreen.tsx";

interface debugProps {
	start: number;
	initmessage: string;
}

declare global {
	export let MyGlobalString: string;
	export function myGlobalFunction(): string;
}
let MyGlobalString = "text from external module";

export function myGlobalFunction() {
	console.log("myGlobalFunction called");
	return "hello";
}

export function setMyGlobalString(newcontent: string) {
	console.log("setMyGlobalString called");
	MyGlobalString = newcontent;
}

//export default function Debug(props: debugProps) {
export default function Debug({ start, initmessage }: debugProps) {
	const [message_external, setmessage_external] = useState("initial");


	return (
		<div class="w-full pt-5">
			<h2>Debug Widget</h2>
			<p>
				<ButtonGreen
					onClick={() => setmessage_external(MyGlobalString)}
				>
					update external message
				</ButtonGreen>
				<textarea
					placeholder="text from external module"
					class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
				>
					{message_external}
				</textarea>
			</p>
		</div>
	);
}
