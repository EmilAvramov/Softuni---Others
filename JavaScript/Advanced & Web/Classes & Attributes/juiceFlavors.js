function juice(data = []) {
    let produced = new Map();
    let leftovers = new Map();
    for (let line of data) {
        let [name, qty] = line.split(" => ");
        let [bottles, leftover] = calculate(qty);
        if (bottles > 0) {
            handleMap(produced, name, bottles);
        }
        if (leftover > 0) {
            handleMap(leftovers, name, leftover);
            if (leftovers.get(name) >= 1000) {
                let [bottles, leftover] = calculate(leftovers.get(name));
                handleMap(produced, name, bottles);
                leftovers.set(name, leftover);
            }
        }
    }

    for (const [k, v] of produced) {
        console.log(`${k} => ${v}`);
    }

    function handleMap(map, name, item) {
        if (!map.has(name)) {
            return map.set(name, item);
        } else {
            return map.set(name, map.get(name) + item);
        }
    }

    function calculate(qty) {
        let bottles = parseInt(qty / 1000);
        let leftover = qty % 1000;
        return [bottles, leftover];
    }
}

juice([
    "Orange => 2000",
    "Peach => 1432",
    "Banana => 450",
    "Peach => 600",
    "Strawberry => 549",
]);

juice([
    "Kiwi => 234",
    "Pear => 2345",
    "Watermelon => 3456",
    "Kiwi => 4567",
    "Pear => 5678",
    "Watermelon => 6789",
]);
