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