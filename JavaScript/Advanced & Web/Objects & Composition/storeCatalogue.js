function storeCatalogue(arr = []) {
    var catalogue = [];
    let letter = "";
    arr.forEach((element) => catalogue.push(element.split(" : ")));
    catalogue.sort((a, b) => (a > b ? 1 : -1));

    catalogue.forEach((element) => {
        if (element[0][0] !== letter) {
            letter = element[0][0];
            console.log(letter);
        }
        console.log(`  ${element[0]}: ${element[1]}`);
    });
}

storeCatalogue([
    "Appricot : 20.4",
    "Fridge : 1500",
    "TV : 1499",
    "Deodorant : 10",
    "Boiler : 300",
    "Apple : 1.25",
    "Anti-Bug Spray : 15",
    "T-Shirt : 10",
]);


storeCatalogue(['Banana : 2',
'Rubic\'s Cube : 5',
'Raspberry P : 4999',
'Rolex : 100000',
'Rollon : 10',
'Rali Car : 2000000',
'Pesho : 0.000001',
'Barrel : 10'])