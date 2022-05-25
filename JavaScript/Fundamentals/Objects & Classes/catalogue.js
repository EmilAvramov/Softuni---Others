function catalogue(products = []) {
    let database = [],
        elements,
        product,
        letter;
    for (let i = 0; i < products.length; i++) {
        elements = products[i].split(" : ");
        product = { name: elements[0], price: parseFloat(elements[1]) };
        database.push(product);
    }
    database = database.sort((a, b) => a.name.localeCompare(b.name));
    for (const product of database) {
        if (product.name.charAt(0).toUpperCase() === letter) {
            console.log(`  ${product.name}: ${product.price}`);
        } else {
            letter = product.name.charAt(0).toUpperCase();
            console.log(letter);
            console.log(`  ${product.name}: ${product.price}`);
        }
    }
}

catalogue([
    "Appricot : 20.4",
    "Fridge : 1500",
    "TV : 1499",
    "Deodorant : 10",
    "Boiler : 300",
    "Apple : 1.25",
    "Anti-Bug Spray : 15",
    "T-Shirt : 10",
]);
