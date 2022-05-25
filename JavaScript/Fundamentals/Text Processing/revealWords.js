function reveal(matches, string) {
    matches = matches.split(", ");
    string = string.split(" ");
    for (let element of string) {
        if (findLength(element) === element.length) {
            for (let match of matches) {
                if (element.length === match.length) {
                    string.splice(string.indexOf(element), 1, match);
                    break;
                }
            }
        }
    }
    console.log(string.join(" "));

    function findLength(word) {
        let count = 0;
        for (let letter of word) {
            if (letter === "*") {
                count++;
            }
        }
        if (count === word.length) {
            return count;
        } else {
            return false;
        }
    }
}

reveal(
    "great",
    "softuni is ***** place for learning new programming languages"
);

reveal(
    "great, learning",
    "softuni is ***** place for ******** new programming languages"
);
