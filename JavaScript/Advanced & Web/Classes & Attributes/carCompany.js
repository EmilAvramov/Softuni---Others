function carCompany(data = []) {
    let carInventory = {};
    for (let line of data) {
        let [brand, model, qty] = line.split(" | ");
        qty = Number(qty);
        if (!carInventory.hasOwnProperty(brand)) {
            carInventory[brand] = [[model, qty]];
        } else {
            let exists = false;
            for (let item of carInventory[brand]) {
                if (item.includes(model)) {
                    item[1] += qty;
                    exists = true;
                    break;
                }
            }
            if (!exists) {
                carInventory[brand].push([model, qty]);
            }
        }
    }

    for (const property in carInventory) {
        console.log(property);
        for (let data of carInventory[property]) {
            console.log(`###${data[0]} -> ${data[1]}`);
        }
    }
}

carCompany([
    "Audi | Q7 | 1000",
    "Audi | Q6 | 100",
    "BMW | X5 | 1000",
    "BMW | X6 | 100",
    "Citroen | C4 | 123",
    "Volga | GAZ-24 | 1000000",
    "Lada | Niva | 1000000",
    "Lada | Jigula | 1000000",
    "Citroen | C4 | 22",
    "Citroen | C5 | 10",
]);
