function cardGame(data = []) {
    function findScore(value) {
        let power = value.split("")[0];
        let color = value.split("")[1];
        let sum = 0;
        power in sets ? (sum += sets[power]) : (sum += Number(power));
        if (Number(color) === 0) {
            sum = sets[value.split("")[2]];
            sum *= 10;
        } else {
            sum *= Number(sets[color]);
        }
        return sum;
    }

    var sets = { J: 11, Q: 12, K: 13, A: 14, S: 4, H: 3, D: 2, C: 1 };
    var map = new Map();
    for (let line of data) {
        let person = line.split(": ")[0];
        let cards = line.split(": ")[1];
        !map.has(person)
            ? map.set(person, cards)
            : map.set(person, map.get(person) + ", " + cards);
    }
    for (let [key, value] of map) {
        let finalSum = 0;
        value = [...new Set(value.split(", "))];
        value.forEach((card) => (finalSum += findScore(card)));
        map.set(key, finalSum);
    }
    for (const [key, value] of map) {
        console.log(`${key}: ${value}`);
    }
}

cardGame([
    "Peter: 2C, 4H, 9H, AS, QS",
    "Tomas: 3H, 10S, JC, KD, 5S, 10S",
    "Andrea: QH, QC, QS, QD",
    "Tomas: 6H, 7S, KC, KD, 5S, 10C",
    "Andrea: QH, QC, JS, JD, JC",
    "Peter: JD, JD, JD, JD, JD, JD",
]);
