//@ts-check

/**
 * @param {any[]} array
 */
function meetings(array) {
    let booked = {};
    array.forEach((element) => {
        let weekDay = element.split(" ")[0];
        let name = element.split(" ")[1];
        if (Object.keys(booked).includes(weekDay)) {
            console.log(`Conflict on ${weekDay}!`);
        } else {
            console.log(`Scheduled for ${weekDay}`);
            booked[weekDay] = name;
        }
    });
    for (const property in booked) {
        console.log(`${property} -> ${booked[property]}`);
    }
}

//meetings(["Monday Peter", "Wednesday Bill", "Monday Tim", "Friday Tim"]);

meetings([
    "Friday Bob",
    "Saturday Ted",
    "Monday Bill",
    "Monday John",
    "Wednesday George",
]);
