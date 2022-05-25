function travelTime(data = []) {
    function addData(array = [], elements = []) {
        for (let i = 0; i < elements.length; i += 2) {
            let index = array.indexOf(elements[i]);
            if (index >= 0) {
                if (Number(elements[i + 1]) < Number(array[index + 1])) {
                    array.splice(index + 1, 1, elements[i + 1]);
                }
            } else {
                array.push(elements[i]);
                array.push(elements[i + 1]);
            }
        }
        return array;
    }

    var map = new Map();
    data = data.sort((a, b) => {
        if (a.split(" > ")[0].toLowerCase() > b.split(" > ")[0].toLowerCase()) {
            return 1;
        } else {
            return -1;
        }
    });
    for (let line of data) {
        let country = line.split(" > ")[0];
        let town = line.split(" > ")[1];
        let cost = line.split(" > ")[2];
        if (!map.has(country)) {
            map.set(country, [town, cost]);
        } else {
            for (let [key, value] of map) {
                if (key === country && town === value[0] && cost < value[1]) {
                    if (map.size > 1) {
                        let added = addData(map.get(country), [town, cost]);
                        map.set(country, added);
                        break;
                    } else {
                        map.set(country, [town, cost]);
                        break;
                    }
                } else {
                    let added = addData(map.get(country), [town, cost]);
                    map.set(country, added);
                    break;
                }
            }
        }
    }
    for (let [key, value] of map) {
        let temp = [];
        let result = "";
        for (let i = 0; i < value.length; i += 2) {
            temp.push([value[i], value[i + 1]]);
        }
        temp = temp.sort((a, b) => (Number(a[1]) > Number(b[1]) ? 1 : -1));
        map.set(key, temp);
        result += key + " -> ";
        for (let item of temp) {
            temp.indexOf(item) !== temp.length - 1
                ? (result += item.join(" -> ") + " ")
                : (result += item.join(" -> "));
        }
        console.log(result);
    }
}

travelTime([
    "Bulgaria > Sofia > 500",
    "Bulgaria > Sopot > 800",
    "France > Paris > 2000",
    "Albania > Tirana > 1000",
    "Bulgaria > Sofia > 200",
]);

travelTime([
    "Bulgaria > Sofia > 25000",
    "Bulgaria > Sofia > 25000",
    "Kalimdor > Orgrimar > 25000",
    "Albania > Tirana > 25000",
    "Bulgaria > Varna > 25010",
    "Bulgaria > Lukovit > 10",
]);

travelTime([
    "Bulgaria > Sofia > 25000",
    "aaa > Sofia > 1",
    "aa > Orgrimar > 0",
    "Albania > Tirana > 25000",
    "zz > Aarna > 25010",
    "Bulgaria > Lukovit > 10"
]);
