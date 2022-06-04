function printDeckOfCards(cards = []) {
    let result = [];
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

    for (let card of cards) {
        let tokens = card.split("");
        let suits = tokens.pop();
        let face = tokens.join("");

        if (validFaces.includes(face) && validSuits.hasOwnProperty(suits)) {
            result.push(createCard(face, suits));
        } else {
            throw Error(`Invalid card: ${face + suits}`);
        }
    }

    console.log(result.join(" "));
    function createCard(faceV, suitsV) {
        return faceV + validSuits[suitsV];
    }
}

printDeckOfCards(["AS", "10D", "KH", "2C"]);
printDeckOfCards(["5S", "3D", "QD", "1C"]);
