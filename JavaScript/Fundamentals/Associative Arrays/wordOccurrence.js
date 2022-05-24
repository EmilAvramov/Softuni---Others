function countWords(data) {
    var map = new Map();
    var sorted = [];
    for (let line of data) {
        if (!map.has(line)) {
            map.set(line, 1);
        } else {
            let count = map.get(line);
            map.set(line, count + 1);
        }
    }
    sorted = [...map.entries()].sort((a, b) => {
        return b[1] - a[1];
    });
    for (const kvp of sorted) {
        console.log(`${kvp[0]} -> ${kvp[1]} times`);
    }
}

countWords([
    "Here",
    "is",
    "the",
    "first",
    "sentence",
    "Here",
    "is",
    "another",
    "sentence",
    "And",
    "finally",
    "the",
    "third",
    "sentence",
]);
console.log("break");
countWords(["dog", "bye", "city", "dog", "dad", "boys", "ginger"]);
