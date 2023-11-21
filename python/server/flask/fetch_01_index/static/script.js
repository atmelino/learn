function getHello() {
    const url = 'http://localhost:8989'
    // const url = 'http://localhost:5000'
    fetch(url)
    .then(response => response.json())  
    .then(json => {
        console.log(json);
        document.getElementById("demo").innerHTML = JSON.stringify(json)
    })
}