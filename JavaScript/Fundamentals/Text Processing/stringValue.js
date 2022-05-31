function stringValue(arr = []) {
    var string = arr[0];
    const command = arr[1];
    let sumUpper = 0;
    let sumLower = 0;
    for (let letter of string) {
        if (letter.charCodeAt(0) > 64 && letter.charCodeAt(0) < 91) {
            sumUpper += letter.charCodeAt(0);
        } else if (letter.charCodeAt(0) > 96 && letter.charCodeAt(0) < 123) {
            sumLower += letter.charCodeAt(0);
        }
    }
    if (command === "LOWERCASE") {
        console.log(`The total sum is: ${sumLower}`);
    } else {
        console.log(`The total sum is: ${sumUpper}`);
    }
}

stringValue(["HelloFromMyAwesomePROGRAM", "LOWERCASE"]);
stringValue(["AC/DC", "UPPERCASE"]);
