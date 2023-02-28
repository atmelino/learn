import { Card } from "../components/Card.tsx";
import Debug from "../islands/Debug.tsx";
import Debug_user from "./Debug_user.tsx";

export default function Body() {

	return (
		<div class=" space-y-4 mx-auto max-w-screen-md flex flex-col justify-center items-center">
			<Card>
				<Debug_user start={1} initmessage="hello" />
			</Card>
			<Card>
				<Debug start={1} initmessage="hello" />
			</Card>
		</div>
	);
}
