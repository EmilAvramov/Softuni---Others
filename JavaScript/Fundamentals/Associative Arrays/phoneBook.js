//@ts-check

/**
 * @param {any[]} arr
 */
function person(arr) {
    var uniques = {};
    arr.forEach((element) => {
        let person = element.split(" ")[0];
        let phone = element.split(" ")[1];
        uniques[person] = phone;
    });
    for (const property in uniques) {
        console.log(`${property} -> ${uniques[property]}`);
    }
}

person([
    "Tim 0834212554",
    "Peter 0877547887",
    "Bill 0896543112",
    "Tim 0876566344",
]);
