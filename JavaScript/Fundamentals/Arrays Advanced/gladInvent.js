function gladInvent(arr = []) {
    let inventory, operations, command, item, index, upgrade;
    [inventory, ...operations] = arr;
    inventory = inventory.split(" ");
    operations.forEach((operation) => {
        [command, ...item] = operation.split(" ");
        switch (command) {
            case "Buy":
                if (!inventory.includes(item[0])) {
                    inventory.push(item[0]);
                }
                break;
            case "Trash":
                if (inventory.includes(item[0])) {
                    index = inventory.indexOf(item[0]);
                    inventory.splice(index, 1);
                }
                break;
            case "Repair":
                if (inventory.includes(item[0])) {
                    index = inventory.indexOf(item[0]);
                    inventory.splice(index, 1);
                    inventory.push(item[0]);
                }
                break;
            default:
                upgrade = item[0].split("-")[1];
                item = item[0].split("-")[0];
                if (inventory.includes(item)) {
                    index = inventory.indexOf(item);
                    inventory.splice(index + 1, 0, item + ":" + upgrade);
                }
                break;
        }
    });
    console.log(inventory.join(" "));
}

gladInvent([
    "SWORD Shield Spear",
    "Buy Bag",
    "Trash Shield",
    "Repair Spear",
    "Upgrade SWORD-Steel",
]);

gladInvent([
    "SWORD Shield Spear",
    "Trash Bow",
    "Repair Shield",
    "Upgrade Helmet-V",
]);
