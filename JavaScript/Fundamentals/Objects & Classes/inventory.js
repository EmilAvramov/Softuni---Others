function inventory(heroes = []) {
    var allHeroes = [];
    let name, level, items;
    heroes = heroes.sort((a, b) => {
        return a.split("/")[1] - b.split("/")[1];
    });
    heroes.forEach((element) => {
        [name, level, ...items] = element.split(" / ");
        allHeroes.push({ name, level, items });
    });
    allHeroes.forEach((element) => {
        console.log(`Hero: ${element.name}`);
        console.log(`level => ${element.level}`);
        console.log(`items => ${element.items}`);
    });
}

inventory([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara",
]);