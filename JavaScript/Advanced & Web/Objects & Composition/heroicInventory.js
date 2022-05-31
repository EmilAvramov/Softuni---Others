function heroes(arr = []) {
    var heroes = [];
    for (let hero of arr) {
        let [name, level, ...items] = hero.split(" / ");
        level = Number(level);
        if (items[0]) {
            items = items ? items[0].split(", ") : [];
        } else {
            items = [];
        }

        heroes.push({ name, level, items });
    }

    console.log(JSON.stringify(heroes));
}

heroes([
    "Isacc / 25 / Apple, GravityGun",
    "Derek / 12 / BarrelVest, DestructionSword",
    "Hes / 1 / Desolator, Sentinel, Antara",
]);

heroes(["Jake / 1000"]);
