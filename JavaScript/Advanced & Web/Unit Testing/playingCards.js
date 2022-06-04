function cards(str1, str2) {
    const validFaces = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "J",
        "Q",
        "K",
        "A",
    ];
    const validSuits = {
        S: "\u2660",
        H: "\u2665",
        D: "\u2666",
        C: "\u2663",
    };
    try {
        if (!validFaces.includes(str1)) {
            throw new Error("Error");
        } else if (!validSuits.hasOwnProperty(str2)) {
            throw new Error("Error");
        } else {
            cards.toString = function () {
                return (str1 + validSuits[str2]).toString();
            };
            return str1 + validSuits[str2];
        }
    } catch (e) {
        return e;
    }
}

console.log(cards("A", "S"));
console.log(cards("10", "H"));
console.log(cards("1", "C"));
