//@ts-check

/**
 * @param {string} name
 * @param {number} population
 * @param {number} treasury
 */
function cityTaxes(name, population, treasury) {
    var city = {
        name: name,
        population: population,
        treasury: treasury,
        taxRate: 10,
        collectTaxes: function () {
            this.treasury += this.population * this.taxRate;
        },
        applyGrowth: function (/** @type {number} */ percentage) {
            this.population += this.population * (percentage / 100);
        },
        applyRecession: function (/** @type {number} */ percentage) {
            this.treasury -= this.treasury * (percentage / 100);
        },
    };
    return city;
}

const city = cityTaxes("Tortuga", 7000, 15000);
city.collectTaxes();
console.log(city.treasury);
city.applyGrowth(5);
console.log(city.population);
city.applyRecession(10)
console.log(city.treasury)