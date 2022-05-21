function store(stock = [], ordered = []) {
    let stockObject = {};
    for (let i = 0; i < stock.length; i += 2) {
        stockObject[stock[i]] = Number(stock[i + 1]);
    }
    for (let i = 0; i < ordered.length; i += 2) {
        if (ordered[i] in stockObject) {
            stockObject[ordered[i]] += Number(ordered[i + 1]);
        } else {
            stockObject[ordered[i]] = Number(ordered[i + 1]);
        }
    }
    for (const property in stockObject) {
        console.log(`${property} -> ${stockObject[property]}`);
    }
}

store(
    ["Chips", "5", "CocaCola", "9", "Bananas", "14", "Pasta", "4", "Beer", "2"],
    [
        "Flour",
        "44",
        "Oil",
        "12",
        "Pasta",
        "7",
        "Tomatoes",
        "70",
        "Bananas",
        "30",
    ]
);
