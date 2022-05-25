function partyTime(data = []) {
    let regular = [];
    let vip = [];
    let invited = data.splice(0, data.indexOf("PARTY"));
    data.splice(0, 1);
    invited.forEach((guest) =>
        /^\d+/.test(guest) ? vip.push(guest) : regular.push(guest)
    );
    data.forEach((guest) => {
        if (vip.includes(guest)) {
            vip.splice(vip.indexOf(guest), 1);
        }
        if (regular.includes(guest)) {
            regular.splice(regular.indexOf(guest), 1);
        }
    });
    console.log(regular.length + vip.length);
    vip.forEach((guest) => console.log(guest));
    regular.forEach((guest) => console.log(guest));
}

partyTime([
    "9NoBUajQ",
    "Ce8vwPmE",
    "SVQXQCbc",
    "tSzE5t0p",
    "7IK9Yo0h",
    "PARTY",
    "9NoBUajQ",
    "Ce8vwPmE",
    "SVQXQCbc",
]);

partyTime([
    "m8rfQBvl",
    "fc1oZCE0",
    "UgffRkOn",
    "7ugX7bm0",
    "9CQBGUeJ",
    "2FQZT3uC",
    "dziNz78I",
    "mdSGyQCJ",
    "LjcVpmDL",
    "fPXNHpm1",
    "HTTbwRmM",
    "B5yTkMQi",
    "8N0FThqG",
    "xys2FYzn",
    "MDzcM9ZK",
    "PARTY",
    "2FQZT3uC",
    "dziNz78I",
    "mdSGyQCJ",
    "LjcVpmDL",
    "fPXNHpm1",
    "HTTbwRmM",
    "B5yTkMQi",
    "8N0FThqG",
    "m8rfQBvl",
    "fc1oZCE0",
    "UgffRkOn",
    "7ugX7bm0",
    "9CQBGUeJ",
]);
