//@ts-check

/**
 * @param {string[]} data
 */
function storage(data) {
    let map = new Map();
    for (let line of data) {
        let product = line.split(" ")[0];
        let quantity = Number(line.split(" ")[1]);
        if (!map.has(product)) {
            map.set(product, quantity);
        } else {
            let currentQ = Number(map.get(product));
            map.set(product, currentQ + quantity);
        }
    }

    for (let kvp of map) {
        console.log(`${kvp[0]} -> ${kvp[1]}`);
    }
}

storage(["tomatoes 10", "coffee 5", "olives 100", "coffee 40"]);
