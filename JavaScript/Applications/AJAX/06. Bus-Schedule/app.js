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
    let c_stop = "";
    let next = "";

    // The json is a linked list
    async function depart() {
        start.disabled = true;
        end.disabled = false;
        let stop = await data.then((value) => Object.entries(value));
        if (info.textContent === "Not Connected") {
            c_stop = stop[15][0];
            info.textContent = `Next stop ${c_stop}`;
            next = stop[15][1].next;
        } else if (next === "depot") {
            info.textContent = "Error";
        } else {
            for (let i = 0; i < Object.values(stop).length; i++) {
                if (Object.values(stop)[i][0] === next) {
                    idx = Object.values(stop)[i][0];
                    c_stop = Object.values(stop)[i][1].name;
                    info.textContent = `Next stop ${c_stop}`;
                    next = Object.values(stop)[i][1].next;
                    break;
                }
            }
        }
    }

    function arrive() {
        start.disabled = false;
        end.disabled = true;
        info.textContent = `Arriving at ${c_stop}`;
    }

    return {
        depart,
        arrive,
    };
}

let result = solve();
