//@ts-check

/**
 * @param {any[]} data
 */
function addressBook(data) {
    var dataSort = [];
    var dataObject = {};
    data.forEach((/** @type {string} */ element) => {
        let name = element.split(":")[0];
        let location = element.split(":")[1];
        dataObject[name] = location;
    });
    for (const property in dataObject) {
        dataSort.push([property, dataObject[property]]);
    }
    dataSort = dataSort.sort((a, b) => {
        return a[0] > b[0] ? 1 : -1;
    });
    dataSort.forEach((element) => {
        console.log(`${element[0]} -> ${element[1]}`);
    });
}

addressBook([
    "Tim:Doe Crossing",
    "Bill:Nelson Place",
    "Peter:Carlyle Ave",
    "Bill:Ornery Rd",
]);

addressBook([
    "Bob:Huxley Rd",
    "John:Milwaukee Crossing",
    "Peter:Fordem Ave",
    "Bob:Redwing Ave",
    "George:Mesta Crossing",
    "Ted:Gateway Way",
    "Bill:Gateway Way",
    "John:Grover Rd",
    "Peter:Huxley Rd",
    "Jeff:Gateway Way",
    "Jeff:Huxley Rd",
]);
