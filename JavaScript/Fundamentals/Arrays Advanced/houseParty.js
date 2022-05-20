function houseParty(arr) {
    let guests = [];
    let name = "";
    let status = true;
    arr.forEach((guest) => {
        name = guest.split(" ")[0];
        if (guest.includes("not")) {
            status = false;
        }
        if (guests.includes(name) && status === true) {
            console.log(`${name} is already in the list!`);
        } else if (guests.includes(name) && status === false) {
            guests = guests.filter((x) => x !== name);
            status = true;
        } else if (!guests.includes(name) && status === true) {
            guests.push(name);
        } else if (!guests.includes(name) && status === false) {
            console.log(`${name} is not in the list!`);
            status = true;
        }
    });
    console.log(guests.join("\n"));
}

houseParty([
    "Allie is going!",
    "George is going!",
    "John is not going!",
    "George is not going!",
]);

houseParty([
    "Tom is going!",
    "Annie is going!",
    "Tom is going!",
    "Garry is going!",
    "Jerry is going!",
]);
