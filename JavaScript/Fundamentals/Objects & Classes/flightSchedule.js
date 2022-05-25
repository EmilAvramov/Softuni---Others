//@ts-check

/**
 * @param {Array} input
 */
function flightSchedule(input) {
    const flights = input[0];
    const statusChanges = input[1];
    const toCheck = input[2];
    var withChange = [];
    var noChange = [];
    var matched = false;
    for (let i = 0; i < flights.length; i++) {
        let flight, destination;
        [flight, ...destination] = flights[i].split(" ");
        destination = destination.join(" ");
        for (let j = 0; j < statusChanges.length; j++) {
            let flightMatch = statusChanges[j].split(" ")[0];
            let status = statusChanges[j].split(" ")[1];
            if (flightMatch === flight) {
                withChange.push({ Destination: destination, Status: status });
                matched = true;
            }
        }
        if (!matched) {
            noChange.push({ Destination: destination, Status: "Ready to fly" });
        }
        matched = false;
    }

    if (toCheck[0] === "Ready to fly") {
        noChange.forEach((flight) => {
            console.log(flight);
        });
    } else {
        withChange.forEach((flight) => {
            console.log(flight);
        });
    }
}

flightSchedule([
    [
        "WN269 Delaware",
        "FL2269 Oregon",
        "WN498 Las Vegas",
        "WN3145 Ohio",
        "WN612 Alabama",
        "WN4010 New York",
        "WN1173 California",
        "DL2120 Texas",
        "KL5744 Illinois",
        "WN678 Pennsylvania",
    ],
    [
        "DL2120 Cancelled",
        "WN612 Cancelled",
        "WN1173 Cancelled",
        "SK430 Cancelled",
    ],
    ["Cancelled"],
]);
flightSchedule([
    [
        "WN269 Delaware",
        "FL2269 Oregon",
        "WN498 Las Vegas",
        "WN3145 Ohio",
        "WN612 Alabama",
        "WN4010 New York",
        "WN1173 California",
        "DL2120 Texas",
        "KL5744 Illinois",
        "WN678 Pennsylvania",
    ],
    [
        "DL2120 Cancelled",
        "WN612 Cancelled",
        "WN1173 Cancelled",
        "SK330 Cancelled",
    ],
    ["Ready to fly"],
]);
