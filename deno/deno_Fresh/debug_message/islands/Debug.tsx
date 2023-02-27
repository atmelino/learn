import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { ButtonGreen } from "../components/ButtonGreen.tsx";
import { MyIP } from "../components/MyIP.tsx";

interface debugProps {
	start: number;
	initmessage: string;
}

declare global {
	export let MyGlobalString: string;
}
let MyGlobalString = "text from external module";

export function setMyGlobalString(newcontent: string) {
	console.log("setMyGlobalString called");
	MyGlobalString = newcontent;
}

export default function Debug(props: debugProps) {
	const [message_in_div, setmessage_in_div] = useState(props.initmessage);
	const [message_in_textarea, setmessage_in_textarea] = useState(props.initmessage);
	const [message_in_textarea_component, setmessage_in_textarea_component] = useState(props.initmessage);
	const [myIPstring, setDebug] = useState("initial");
	const [message_external, setMyGlobalString] = useState("initial");

	function setDebugText(message: string) {
		setmessage_in_div(message);
	}

	function setDebugmessage_in_textarea(message: string) {
		//alert("hi");
		setmessage_in_textarea(message);
	}

	return (
		<div class="flex flex-col w-full ">
			<h2>Debug Widget</h2>

			<ButtonGreen
				onClick={() => setMyGlobalString(MyGlobalString)}
			>
				update external message
			</ButtonGreen>
			<textarea
				placeholder="text from external module"
				class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
			>
				{message_external}
			</textarea>
			<ButtonGreen
				onClick={() => setDebugText(message_in_div + "text")}
			>
				debug message in div
			</ButtonGreen>
			{message_in_div}
			<ButtonGreen
				onClick={() => setDebugmessage_in_textarea(message_in_textarea + "text")}
			>
				debug message in textarea
			</ButtonGreen>
			<div>
				<textarea
					class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
				>
					{message_in_textarea}
				</textarea>
			</div>
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
			<MyIP myIPstring={myIPstring} />
		</div>
	);
}
