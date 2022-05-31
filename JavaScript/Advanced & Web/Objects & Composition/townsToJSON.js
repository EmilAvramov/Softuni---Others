function townsToJSON(arr = []) {
    var towns = [];
    arr.shift();
    for (let data of arr) {
        data = data.slice(2, data.length - 2);
        let [town, lat, lon] = data.split(" | ");
        lat = Number(parseFloat(lat).toFixed(2))
        lon = Number(parseFloat(lon).toFixed(2))
        towns.push({ Town: town, Latitude: lat, Longitude: lon });
    }
    console.log(JSON.stringify(towns));
}

townsToJSON([
    "| Town | Latitude | Longitude |",
    "| Sofia | 42.696552 | 23.32601 |",
    "| Beijing | 39.913818 | 116.363625 |",
]);

townsToJSON(["| Town | Latitude | Longitude |",
    "| Veliko Turnovo | 43.0757 | 25.6172 |",
    "| Monatevideo | 34.50 | 56.11 |"])