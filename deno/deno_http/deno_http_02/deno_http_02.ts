//let resp1 = await fetch("http://localhost");
//console.log(resp1.status); // 200
// console.log(resp1.headers.get("Content-Type")); // "text/html"
// console.log(await resp1.text());

/*
const req = new Request("http://localhost:8000/todos", {
  method: "GET",
});
const resp = await fetch(req);
console.log(resp);
console.log(await resp.text());
*/

async function getNotes() {
  const req = new Request("http://localhost:8000/todos", {
    method: "GET",
  });
  const resp = await fetch(req);
  let ret = await resp.text();
  return ret;
}

async function addNote() {
  const req = new Request("http://localhost:8000/todos", {
    method: "GET",
  });
  const resp = await fetch(req);
  let ret = await resp.text();
  return ret;
}

let myre = getNotes();
console.log(await myre);

//console.log(await getNotes());

export {};
