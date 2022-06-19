function getData() {
    let response = fetch("http://localhost:3030/jsonstore/bus/schedule/").then(
        (response) => response.json()
    );
    return response;
}

function solve() {
    let info = document.getElementById("info");
    let start = document.getElementById("depart");
    let end = document.getElementById("arrive");
    let data = getData();
    let index = 0;
    // The json is a linked list 
    async function depart() {
        let stop = await data.then((value) => Object.entries(value)[index]);
        if (info.textContent === "Not Connected") {
            stop = await data.then((value) => Object.entries(value)[15]);
            info.textContent = stop[1].name;
            index++;
        } else if (index === 14) {
            info.textContent = "Error";
        } else {
            info.textContent = stop[1].name;
            index++;
        }
    } 

    function arrive() {
        console.log("Arrive TODO...");
    }

    return {
        depart,
        arrive,
    };
}

let result = solve();
