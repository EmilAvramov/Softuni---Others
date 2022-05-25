function serialize(arr = []) {
    var data = arr[0];
    var map = new Map();
    for (let i = 0; i < data.length; i++) {
        if (!map.has(data[i])) {
            map.set(data[i], [i]);
        } else {
            let temp = map.get(data[i]);
            temp.push(i);
            map.set(data[i], temp);
        }
    }
    for (let [key, value] of map) {
        console.log(`${key}:${value.join("/")}`);
    }
}

serialize(["abababa"]);
serialize(["avjavamsdmcalsdm"]);
