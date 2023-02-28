import { Card } from "../components/Card.tsx";
import Debug from "../islands/Debug.tsx";
import Debug_user from "./Debug_user.tsx";
import * as mydebug from "../islands/Debug.tsx";
import { useRef, useState } from "preact/hooks";

export default function Body() {
	function setDebugMesssage(uuid: string) {
		console.log("setDebugMesssage called");
    setdebugMessage("456");
	}
	const [debugMessage, setdebugMessage] = useState("123");

	return (
		<div class=" space-y-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
			<Card>
				<Debug_user start={1} initmessage="hello" setDebugMesssage={setDebugMesssage} />
			</Card>
			<Card>
				<Debug start={1} initmessage="hello" setDebugMesssage={setDebugMesssage} debugMessage={debugMessage}/>
			</Card>
		</div>
	);
}
