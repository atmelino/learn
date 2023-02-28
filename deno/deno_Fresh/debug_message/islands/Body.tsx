import { Card } from "../components/Card.tsx";
import Debug from "../islands/Debug.tsx";
import Debug_user from "./Debug_user.tsx";
import * as mydebug from "../islands/Debug.tsx";
import { useRef, useState } from "preact/hooks";

export default function Body() {
	function removeNote(uuid: string) {
		console.log("removenote called");
    setmessage_in_div("456");
	}
	const [debugMessage, setmessage_in_div] = useState("123");

	return (
		<div class=" space-y-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
			<Card>
				<Debug_user start={1} initmessage="hello" removeNote={removeNote} />
			</Card>
			<Card>
				<Debug start={1} initmessage="hello" removeNote={removeNote} debugMessage={debugMessage}/>
			</Card>
		</div>
	);
}
