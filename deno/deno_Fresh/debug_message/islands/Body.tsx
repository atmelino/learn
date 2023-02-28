import { Card } from "../components/Card.tsx";
import Debug from "../islands/Debug.tsx";
import Debug_user from "./Debug_user.tsx";
import { useRef, useState } from "preact/hooks";

export default function Body() {
	function setDebugMesssage(message: string) {
		console.log("setDebugMesssage called");
		//		setdebugMessage("456");
		setdebugMessage(message);
	}
	const [debugMessage, setdebugMessage] = useState("123");

	return (
		<div class=" space-y-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
			<Card>
				<Debug_user initmessage="hello" setDebugMesssage={setDebugMesssage} />
			</Card>
			<Card>
				<Debug initmessage="hello" setDebugMesssage={setDebugMesssage} debugMessage={debugMessage} />
			</Card>
		</div>
	);
}
