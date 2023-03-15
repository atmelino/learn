# fresh project

### Usage

Start the project:

```
deno task start
```

This will watch the project directory and restart as necessary.

make a fresh copy of fresh-remult-todo_client_01 and change the model to fit the database for notekeeper.
Do not update the Fresh by running
deno run -A -r https://fresh.deno.dev/update .
because this will lead to error when adding tailwind.
The fresh version in
import_map.json
will be
$fresh/": "https://deno.land/x/fresh@1.0.1/",
as in the original fresh-remult-todo_client_01.


