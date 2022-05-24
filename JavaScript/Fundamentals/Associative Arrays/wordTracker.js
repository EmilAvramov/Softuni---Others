function wordTracker(data) {
    // var map = new Map();
    // let search,
    //     sorted = [];
    // search = data.shift().split(" ")
    // for (let line of data) {
    //     if (!map.has(line) && search.includes(line)) {
    //         map.set(line, 1);
    //     } else if (map.has(line) && search.includes(line)) {
    //         map.set(line, map.get(line) + 1);
    //     }
    // }
    // sorted = [...map.entries()].sort((a, b) => {
    //     return b[1] - a[1];
    // });
    // for (const item of sorted) {
    //     console.log(`${item[0]} - ${item[1]}`);
    // }
    let search = data.shift().split(" ");
    let found = {};
    search.forEach((word) => (found[word] = 0));
    data.forEach((word) => word in found && found[word]++);
    search.sort((a, b) => found[b] - found[a]);
    search.forEach((word) => console.log(`${word} - ${found[word]}`));
}

wordTracker([
    "this sentence",
    "In",
    "this",
    "sentence",
    "you",
    "have",
    "to",
    "count",
    "the",
    "occurrences",
    "of",
    "the",
    "words",
    "this",
    "and",
    "sentence",
    "because",
    "this",
    "is",
    "your",
    "task",
]);

wordTracker([
    "is the",
    "first",
    "sentence",
    "Here",
    "is",
    "another",
    "the",
    "And",
    "finally",
    "the",
    "the",
    "sentence",
]);
