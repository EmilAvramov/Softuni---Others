function treasureFinder(arr = []) {
    var key = arr.shift().split(" ");
    arr.pop();
    let coords = [];
    let count = 0;
    for (let line of arr) {
        let tempWord = "";
        for (let letter of line) {
            let tempLetter = letter.charCodeAt(0) - key[count];
            tempWord += String.fromCodePoint(tempLetter);
            count++;
            if (count === key.length) {
                count = 0;
            }
        }
        coords.push(tempWord);
        count = 0;
    }
    for (let coord of coords) {
        let material, location;
        material = coord.split("&")[1];
        location = coord.split("<")[1];
        if (location) {
            location = location.slice(0, location.length - 1);
        }
        if (material) {
            console.log(
                `Found ${coord.match(material)} at ${coord.match(location)}`
            );
        }
    }
}

treasureFinder([
    "1 2 1 3",
    "ikegfp'jpne)bv=41P83X@",
    "ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA",
    "find",
]);

treasureFinder([
    "1 2 1 3",
    "asdf",
    "udasd",
    "find",
]);
