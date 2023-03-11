import { Entity, Fields } from "remult";

@Entity("tasks", {
    allowApiCrud: true
})
export class Task {
    @Fields.uuid()
    id!: number;

    @Fields.date()
    timestamp='';

    @Fields.string()
    title = '';

    @Fields.string()
    noteId = '';

}

// id SERIAL PRIMARY KEY,
// timestamp TIMESTAMP NOT NULL,
// noteId TEXT NOT NULL,
// note TEXT NOT NULL