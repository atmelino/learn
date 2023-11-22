function getHello() {

    const url = 'http://localhost:8989'
    fetch(url)
        .then(response => response.json())
        .then(json => {
            printlnMessage('resultsText', JSON.stringify(json));
            printlnMessage('resultsText', JSON.stringify(json.image));
            // newimg = "static/%s" % json.image;
            newimg = "static/" + json.image;
            printlnMessage('resultsText', newimg);
            
            console.log(json);
            const img = document.getElementById("nn");
            img.src = "static/nn_02.svg";
            img.src = newimg;
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