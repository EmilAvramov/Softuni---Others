function getData(id) {
    const url = "http://localhost:3030/jsonstore/bus/businfo/" + id;
    const response = fetch(url)
        .then((response) => response.json())
        .then((data) => data)
        .catch((error) => error);
    return response;
}

let input = document.getElementById("stopId");
let result = document.getElementById("stopName");
let list = document.getElementById("buses");

async function getInfo() {
    let output = await getData(input.value);
    result.textContent = output.name;
    try {
        list.textContent = "";
        for (let property of Object.entries(output.buses)) {
            let e = document.createElement("li");
            e.textContent = `Bus ${property[0]} arrives in ${property[1]} minutes`;
            list.appendChild(e);
        }
    } catch (error) {
        result.textContent = "Error";
    }
}
