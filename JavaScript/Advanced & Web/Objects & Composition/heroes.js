function heroes() {
    function cast(spell) {
        this.mana--;
        console.log(`${this.name} casts ${spell}`);
    }

    function fight() {
        this.stamina--;
        console.log(`${this.name} slashes at the foe!`);
    }

    return {
        mage: (name) => {
            return {
                name: name,
                health: 100,
                mana: 100,
                cast: cast,
            };
        },
        fighter: (name) => {
            return {
                name: name,
                health: 100,
                stamina: 100,
                fight: fight,
            };
        },
    };
}

let create = heroes();
const scorcher = create.mage("Scorcher");
scorcher.cast("fireball");
scorcher.cast("thunder");
scorcher.cast("light");

const scorcher2 = create.fighter("Scorcher 2");
scorcher2.fight();

console.log(scorcher2.stamina);
console.log(scorcher.mana);
