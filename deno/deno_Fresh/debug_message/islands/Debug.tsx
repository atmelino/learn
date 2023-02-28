import { useRef, useState } from "preact/hooks";
import TextArea from "../components/Textarea.tsx";
import { ButtonGreen } from "../components/ButtonGreen.tsx";

interface debugProps {
	start: number;
	initmessage: string;
	setDebugMesssage: (s: string) => void;
	debugMessage: string;
}

export default function Debug({ start, initmessage, setDebugMesssage, debugMessage }: debugProps) {
	const [message_in_div, setmessage_in_div] = useState(initmessage);
	const [message_in_textarea, setmessage_in_textarea] = useState(initmessage);
	const [message_in_textarea_component, setmessage_in_textarea_component] = useState(initmessage);
	const [message_external, setmessage_external] = useState("initial");

	function setDebugText(message: string) {
		setmessage_in_div(message);
		setDebugMesssage("");
	}

	return (
		<div class="w-full pt-5">
			<h2 class="text-lg font-medium text-gray-900 ">Debug Widget</h2>

			<p>
				debug message in div
				<div class="border-1 border-green-900 border-solid  w-full h-12">
					{debugMessage}
				</div>
			</p>
			<p>
				debug message in textarea
				<textarea
					class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
				>
					{debugMessage}
				</textarea>
			</p>
			<p>
				debug message in Textarea component
				<TextArea
					placeholder="text here..."
					rows={3}
					onChange={() => alert("changed")}
				>
					{debugMessage}
				</TextArea>
			</p>
		</div>
	);
}
