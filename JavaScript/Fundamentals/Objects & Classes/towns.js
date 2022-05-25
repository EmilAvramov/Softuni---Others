function towns(arr = []) {
    let allTowns = [];
    let temp = [];
    arr.forEach((info) => {
        temp = info.split(" | ");
        temp[1] = Number(temp[1]).toFixed(2);
        temp[2] = Number(temp[2]).toFixed(2);
        allTowns.push({ town: temp[0], latitude: temp[1], longitude: temp[2] });
    });
    allTowns.forEach((town) => {
        console.log(town);
    });
}

towns(["Sofia | 42.696552 | 23.32601", "Beijing | 39.913818 | 116.363625"]);
