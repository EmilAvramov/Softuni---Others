function lowestPrice(arr = []) {
    var map = new Map();
    for (let line of arr) {
        let [town, product, price] = line.split(" | ");
        if (!map.has(product)) {
            map.set(product, [price, town]);
        } else {
            if (map.get(product)[1] === town) {
                map.set(product, [price, town]);
            } else if (Number(map.get(product)[0]) > Number(price)) {
                map.set(product, [price, town]);
            }
        }
    }
    for (const [key, value] of map) {
        console.log(`${key} -> ${value[0]} (${value[1]})`);
    }
}

lowestPrice([
    "Sample Town | Sample Product | 1000",
    "Sample Town | Orange | 2",
    "Sample Town | Peach | 1",
    "Sofia | Orange | 3",
    "Sofia | Peach | 2",
    "New York | Sample Product | 1000.1",
    "New York | Burger | 10",
]);
console.log("-----");

lowestPrice([
    "Sofia City | Audi | 100000",
    "Sofia City | BMW | 100000",
    "Sofia City | Mitsubishi | 10000",
    "Sofia City | Mercedes | 10000",
    "Sofia City | NoOffenseToCarLovers | 0",
    "Mexico City | Audi | 1000",
    "Mexico City | BMW | 99999",
    "Mexico City | Mitsubishi | 10000",
    "New York City | Mitsubishi | 1000",
    "Washington City | Mercedes | 1000",
]);
