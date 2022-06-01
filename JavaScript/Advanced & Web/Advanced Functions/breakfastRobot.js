function solution() {
    const library = {
        "apple": {carbohydrate: 1, flavour: 2 },
        "lemonade": {carbohydrate: 10, flavour: 20 },
        "burger": {carbohydrate: 5, fat: 7, flavour: 3 },
        "eggs": {protein: 5, fat: 1, flavour: 1 },
        "turkey": {protein: 10, carbohydrate: 10, fat: 10, flavour: 10 },
    };
    let output = "";
    var stock = new Map();
    stock.set("protein", 0);
    stock.set("carbohydrate", 0);
    stock.set("fat", 0);
    stock.set("flavour", 0);

    var commands = {
        restock: (arg) => {
            let [el, qty] = [...arg];
            qty = Number(qty);
            stock.set(el, stock.get(el) + qty);
            output = "Success";
        },
        prepare: (arg) => {
            let [recipe, qty] = [...arg];
            qty = Number(qty);
            for (let obj of Object.keys(library)) {
                if (obj === recipe) {
                    let ingr = Object.keys(library[obj]);
                    let count = 0;
                    for (let item of ingr) {
                        if (stock.get(item) * qty >= library[obj][item]) {
                            count++;
                        } else {
                            output = `Error: not enough ${item} in stock`;
                            break;
                        }
                    }
                    if (count === ingr.length) {
                        for (let item of ingr) {
                            stock.set(item, stock.get(item) - library[obj][item] * qty);
                        }
                        output = "Success";
                    }
                }
            };
        },
        report: () => {
            output = `protein=${stock.get("protein")} carbohydrate=${stock.get("carbohydrate"
            )} fat=${stock.get("fat")} flavour=${stock.get("flavour")}`;
        },
    };

    return (arg) => {
        let [cmd,...args] = arg.split(" ");
        commands[cmd](args);
        return output;
    };
}

let manager = solution();
console.log(manager("restock flavour 50")); // Success
console.log(manager("prepare lemonade 4")); // Error: not enough carbohydrate in stock
console.log(manager("report"));
console.log(manager("prepare turkey 1"));
console.log(manager("restock protein 10"));
console.log(manager("prepare turkey 1"));
console.log(manager("restock fat 10"))
console.log(manager("prepare turkey 1"))