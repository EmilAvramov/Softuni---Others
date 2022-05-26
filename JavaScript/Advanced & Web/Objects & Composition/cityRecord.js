//@ts-check

/**
 * @param {string} name
 * @param {number} population
 * @param {number} treasury
 */
function record(name, population, treasury) {
    return { name, population, treasury };
}

console.log(record("Tortuga", 7000, 15000));
