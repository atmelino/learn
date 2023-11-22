function getHello() {
    // printlnMessage('resultsText',myString);

    const url = 'http://localhost:8989'
    // const url = 'http://localhost:5000'
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        printlnMessage('resultsText',json);

        console.log(json);
        document.getElementById("demo").innerHTML = JSON.stringify(json)
        document.getElementById("image").innerHTML = json.image
        const img = document.getElementById("nn");
        img.src = "static/nn_02.svg";
        newimg = "static/%s" % json.image;
        document.getElementById("image").innerHTML = newimg

    })
}

function printMessage(target, message) {
	elementId = document.getElementById(target);
	if (elementId != null) {
		elementId.innerHTML += message;
		elementId.scrollTop = elementId.scrollHeight;
	}
}

function printlnMessage(target, message) {
	elementId = document.getElementById(target);
	if (elementId != null) {
		printMessage(target, message);
		elementId.innerHTML += '\n';
	}
}

function clearMessage(target) {
	document.getElementById(target).innerHTML = '';
}