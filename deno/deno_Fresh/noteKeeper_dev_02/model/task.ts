import { Entity, Fields } from "remult";

@Entity("notes", {
    allowApiCrud: true
})
export class Task {
    @Fields.uuid()
    id!: string;

    //@Fields.date()
    //timestamp='';

    @Fields.date()
    timestamp = new Date()

    @Fields.string()
    note = '';

}

// id SERIAL PRIMARY KEY,
// timestamp TIMESTAMP NOT NULL,
// noteId TEXT NOT NULL,
// note TEXT NOT NULL

