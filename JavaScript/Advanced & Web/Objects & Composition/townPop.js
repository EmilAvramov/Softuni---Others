//@ts-check

/**
 * @param {any} data
 */
function townPopulation(data) {
    var map = new Map();
    for (let line of data) {
        let town = line.split(" <-> ")[0];
        let population = Number(line.split(" <-> ")[1]);
        if (!map.has(town)) {
            map.set(town, population);
        } else {
            map.set(town, map.get(town) + population);
        }
    }
    for (const [key, value] of map) {
        console.log(`${key} : ${value}`);
    }
}

townPopulation([
    "Sofia <-> 1200000",
    "Montana <-> 20000",
    "New York <-> 10000000",
    "Washington <-> 2345000",
    "Las Vegas <-> 1000000",
]);

townPopulation([
    "Istanbul <-> 100000",
    "Honk Kong <-> 2100004",
    "Jerusalem <-> 2352344",
    "Mexico City <-> 23401925",
    "Istanbul <-> 1000",
]);
