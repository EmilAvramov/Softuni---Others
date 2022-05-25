function treasureFinder(arr = []) {
    var key = arr.shift().split(" ");
    const command = arr.pop();
    let coords = [];
    let count = 0;
    var material = /&(\w+?)&/;
    var location = /<(\w+?)>/;
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
        console.log(
            `Found ${coord.match(material)[1]} at ${coord.match(location)[1]}`
        );
    }
}

treasureFinder([
    "1 2 1 3",
    "ikegfp'jpne)bv=41P83X@",
    "ujfufKt)Tkmyft'duEprsfjqbvfv=53V55XA",
    "find",
]);