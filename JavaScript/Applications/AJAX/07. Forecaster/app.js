async function getData() {
    let request = await fetch(
        "http://localhost:3030/jsonstore/forecaster/locations"
    );
    return request.json();
}

async function getToday(code) {
    let request = await fetch(
        "http://localhost:3030/jsonstore/forecaster/today/" + code
    );
    return request.json();
}

async function getUpcoming(code) {
    let request = await fetch(
        "http://localhost:3030/jsonstore/forecaster/upcoming/" + code
    );
    return request.json();
}

async function getCode(input) {
    let data = await getData().then((value) => Object.values(value));
    let code = "";
    for (const property of Object.values(data)) {
        if (property.name === input) {
            code = property.code;
        }
    }
    return [getToday(code), getUpcoming(code)];
}

function findSymbol(text) {
    let symbol = "";
    if (text === "Sunny") {
        symbol = "&#x2600;";
    } else if (text === "Partly sunny") {
        symbol = "&#x26C5;";
    } else if (text === "Overcase") {
        symbol = "&#x2601;";
    } else {
        symbol = "&#x2614;";
    }
    return symbol;
}

function createCurrent(city, conditions) {
    let e = document.createElement("div");
    let deg = "&#176;";
    let state = Object.values(conditions)[0];
    let lower = Object.values(conditions)[2];
    let upper = Object.values(conditions)[1];
    e.innerHTML += `${findSymbol(
        state
    )} ${city} ${lower}${deg}/${upper}${deg} ${state}`;
    return e;
}

function createUpcoming(obj) {
    let e = document.createElement("div");

    let deg = "&#176;";

    for (const property of Object.values(obj)) {
        let container = document.createElement("span");
        let sym = document.createElement("p");
        let degrees = document.createElement("p");
        let text = document.createElement("p");
        let state, upper, lower;

        [state, upper, lower] = Object.values(property);
        sym.innerHTML = findSymbol(state);
        degrees.innerHTML = `${lower}${deg}/${upper}${deg}`;
        text.innerHTML = state;
        container.appendChild(sym);
        container.appendChild(degrees);
        container.appendChild(text);
        container.style.display = "inline-block";
        container.style.padding = "0px 30px";
        container.style.width = "100px";
        e.appendChild(container);
    }
    return e;
}

let input = document.getElementById("location");
let button = document.getElementById("submit");
let current = document.getElementById("current");
let upcoming = document.getElementById("upcoming");
let forecast = document.getElementById("forecast");

button.addEventListener("click", () => {
    let inputData = input.value;
    forecast.style.display = "block";

    let response = () => {
        let data = getCode(inputData)
            .then((value) => value[0])
            .then((value) => JSON.stringify(value))
            .then((value) => JSON.parse(value))
            .then((data) => {
                current.removeChild(current.lastChild);
                let city = Object.values(data)[1];
                let conditions = Object.values(data)[0];
                let el = createCurrent(city, conditions);
                current.appendChild(el);
            });
        return data;
    };

    let upcomingData = () => {
        let data = getCode(inputData)
            .then((value) => value[1])
            .then((value) => JSON.stringify(value))
            .then((value) => JSON.parse(value))
            .then((data) => {
                upcoming.removeChild(upcoming.lastChild);
                let days = Object.values(data)[0];
                let el = createUpcoming(days);
                upcoming.appendChild(el);
            });
        return data;
    };
    response();
    upcomingData();
});
