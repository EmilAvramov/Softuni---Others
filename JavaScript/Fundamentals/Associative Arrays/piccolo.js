function piccolo(data) {
    var parkingLot = [];
    for (let line of data) {
        let action = line.split(",")[0];
        let car = line.split(",")[1];
        if (action === "IN" && !parkingLot.includes(car)) {
            parkingLot.push(car);
        } else if (action === "OUT" && parkingLot.includes(car)) {
            parkingLot.splice(parkingLot.indexOf(car), 1);
        }
    }
    parkingLot = parkingLot.sort((a, b) => (a > b ? 1 : -1));
    if (parkingLot.length === 0) {
        console.log("Parking Lot is Empty");
    } else {
        for (let item of parkingLot) {
            console.log(item);
        }
    }
}

piccolo([
    "IN, CA2844AA",
    "IN, CA1234TA",
    "OUT, CA2844AA",
    "IN, CA9999TT",
    "IN, CA2866HI",
    "OUT, CA1234TA",
    "IN, CA2844AA",
    "OUT, CA2866HI",
    "IN, CA9876HH",
    "IN, CA2822UU",
]);
