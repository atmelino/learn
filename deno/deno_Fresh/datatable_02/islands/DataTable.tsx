import { useEffect, useRef, useState } from "preact/hooks";


export interface DataTableProps {
	// setDebugMesssage: (s: string) => void;
	// debugMessage: string;
	dataArray: object[];
}





export default function DataTable(props: DataTableProps) {
	const keys = Object.keys(props.dataArray[0]);

	useEffect(() => {
	}, [props]);

	return (

		<table class="border-2">
			<tr class="border-2">
				{keys.map((data, index) => {
					// console.log(keys[index]);
					return <th class="border-2">{keys[index]}</th>;
				})}
			</tr>

			{props.dataArray.map((data, index) => {
				// console.log(data);
				// const keys = Object.keys(data);
				return (
					<tr class="border-2" key={index}>
						{keys.map((k) => {
							console.log(data[k as keyof typeof data]);
							return (
								<td class="border-2">{data[k as keyof typeof data]}</td>
							);
						})}
					</tr>
				);
			})}
		</table>

	);
}
