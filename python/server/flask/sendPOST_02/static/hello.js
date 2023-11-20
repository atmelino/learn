function sayHello() {
    // alert("Hello World")
    yourUrl="/"
    value="123"
    var xhr = new XMLHttpRequest();
    xhr.open("POST", yourUrl, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.send(JSON.stringify({
        value: value
    }));

    console.log("sayHello")
    // location.reload();
    console.log("Hello, World!");



 }