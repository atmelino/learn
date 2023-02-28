import TextArea from "../components/Textarea.tsx";

export interface IDebug {
	setDebugMesssage: (s: string) => void;
	debugMessage: string;
}

export default function Debug({ setDebugMesssage, debugMessage }: IDebug) {
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
