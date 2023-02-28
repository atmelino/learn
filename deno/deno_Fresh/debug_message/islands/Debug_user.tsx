import { useRef, useState } from "preact/hooks";
import { ButtonGreen } from "../components/ButtonGreen.tsx";

interface debugProps {
	initmessage: string;
	setDebugMesssage: (s: string) => void;
}

export default function Debug_user(props: debugProps) {
	const noteRef = useRef<HTMLInputElement | null>(null);

	function setDebugText(message: string) {
		console.log("button pressed");
		props.setDebugMesssage(message);
	}

	return (
		<div class="w-full pt-5">
			<h2 class="text-lg font-medium text-gray-900 ">Debug User</h2>
			This element uses the debug element by sending a message to it

			<div class="flex gap-2 w-full">
				<form
					class="flex gap-2 w-full"
					onSubmit={(e) => {
						e.preventDefault();
						if (!noteRef?.current?.value) {
							setDebugText("empty");
							return;
						}
						setDebugText(noteRef?.current?.value ?? "");
						noteRef.current.value = "";
					}}
				>
					<input
						class="w-5/6 border-1 border-gray-500 h-10 rounded p-2"
						defaultValue="test"
						placeholder="Write a new debug message here..."
						type="text"
						ref={noteRef}
					/>
					<ButtonGreen
						type="submit"
						className="bg-green-500 hover:bg-green-700 text-white font-bold py-2 px-4 rounded w-1/2"
					>
						send debug message
					</ButtonGreen>
				</form>
			</div>
		</div>
	);
}
