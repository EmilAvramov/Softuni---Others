function resources(data) {
    var map = new Map();
    for (let i = 0; i < data.length; i += 2) {
        if (!map.has(data[i])) {
            map.set(data[i], Number(data[i + 1]));
        } else {
            map.set(data[i], map.get(data[i]) + Number(data[i + 1]));
        }
    }

    for (const [key, value] of map) {
        console.log(`${key} -> ${value}`);
    }
}

resources(["Gold", "155", "Silver", "10", "Copper", "17"]);

resources(["gold", "155", "silver", "10", "copper", "17", "gold", "15"]);
