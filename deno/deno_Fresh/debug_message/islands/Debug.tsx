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

	function setDebugmessage_in_textarea(message: string) {
		//alert("hi");
		setmessage_in_textarea(message);
	}

	return (
		<div class="w-full pt-5">
			<h2 class="text-lg font-medium text-gray-900 ">Debug Widget</h2>

			{debugMessage}
			<p>
				<ButtonGreen
					onClick={() => setmessage_external(debugMessage)}
				>
					update external message
				</ButtonGreen>
				<textarea
					placeholder="text from external module"
					class={`w-full p-2 border-2 border-gray-300 rounded-md focus:outline-none focus:border-blue-500 `}
				>
					{debugMessage}
				</textarea>
			</p>
			<p>
				<ButtonGreen
					onClick={() => setDebugText(message_in_div + "text")}
				>
					debug message in div
				</ButtonGreen>
				<br></br>
				<div class="border-4 border-green-900 border-solid bg-green-400 w-full h-12">
					{debugMessage}
				</div>
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
					{debugMessage}
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
					{debugMessage}
				</TextArea>
			</p>
		</div>
	);
}
