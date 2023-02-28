import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { ButtonGreen } from "../components/ButtonGreen.tsx";

interface debugProps {
	start: number;
	initmessage: string;
	setDebugMesssage: (s: string) => void;
	debugMessage:string;
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
export default function Debug({ start, initmessage, setDebugMesssage,debugMessage }: debugProps) {
	const [message_in_div, setmessage_in_div] = useState(initmessage);
	const [message_in_textarea, setmessage_in_textarea] = useState(initmessage);
	const [message_in_textarea_component, setmessage_in_textarea_component] = useState(initmessage);
	const [message_external, setmessage_external] = useState("initial");

	function setDebugText(message: string) {
		setmessage_in_div(message);
		setDebugMesssage("");
	}

	function setDebugmessage_in_textarea(message: string) {
		//alert("hi");
		setmessage_in_textarea(message);
	}

	return (
		<div class="w-full pt-5">
			<h2>Debug Widget</h2>
			{debugMessage}
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
			<p>
				<ButtonGreen
					onClick={() => setDebugText(message_in_div + "text")}
				>
					debug message in div
				</ButtonGreen>
				<br></br>
				{message_in_div}
			</p>
			<p>
				<ButtonGreen
					onClick={() => setDebugmessage_in_textarea(message_in_textarea + "text")}
				>
					debug message in textarea
				</ButtonGreen>
			</p>
			<p>
				<textarea
					class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
				>
					{message_in_textarea}
				</textarea>
			</p>
			<p>
				<ButtonGreen
					onClick={() =>
						setmessage_in_textarea_component(
							message_in_textarea_component + "text",
						)}
				>
					debug message in Textarea component
				</ButtonGreen>
				<TextArea
					placeholder="text here..."
					rows={3}
					onChange={() => alert("changed")}
				>
					{message_in_textarea_component}
				</TextArea>
			</p>
		</div>
	);
}
