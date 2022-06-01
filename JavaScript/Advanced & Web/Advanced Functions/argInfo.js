function types(...args) {
    let arr = args;
    var values = [];
    var typeCount = new Map();
    arr.forEach((element) => {
        let type = typeof element;
        values.push(element);
        if (!typeCount.has(type)) {
            typeCount.set(type, 1);
        } else {
            typeCount.set(type, typeCount.get(type) + 1);
        }
    });
    for (let value of values) {
        console.log(`${typeof value}: ${value}`);
    }

    for (const [key, value] of typeCount) {
        console.log(`${key} = ${value}`);
    }
}

types("cat", 42, function () {
    console.log("Hello world!");
});

types({ name: 'bob'}, 3.333, 9.99)
