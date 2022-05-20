function arrayManipulation(arr) {
    let numbers, commands;
    [numbers, ...commands] = arr;
    numbers = numbers.split(" ").map(Number);
    commands.forEach((element) => {
        let command = element.split(" ")[0];
        let num = Number(element.split(" ")[1]);
        if (command === "Add") {
            numbers.push(num);
        } else if (command === "Remove") {
            numbers = numbers.filter((x) => x !== num);
        } else if (command === "RemoveAt") {
            numbers.splice(num, 1);
        } else {
            let idx = element.split(" ")[2];
            numbers.splice(idx, 0, num);
        }
    });
    console.log(numbers.join(" "));
}

arrayManipulation([
    "4 19 2 53 6 43",
    "Add 3",
    "Remove 2",
    "RemoveAt 1",
    "Insert 8 3",
]);

arrayManipulation([
    "6 12 2 65 6 42",
    "Add 8",
    "Remove 12",
    "RemoveAt 3",
    "Insert 6 2",
]);
