function companyUsers(data = []) {
    var map = new Map();
    data = data.sort((a, b) => {
        if (a.split(" -> ")[0] > b.split(" -> ")[0]) {
            return 1;
        } else if (a.split(" -> ")[0] < b.split(" -> ")[0]) {
            return -1;
        } else {
            return 0;
        }
    });
    for (let line of data) {
        let company = line.split(" -> ")[0];
        let employee = line.split(" -> ")[1];
        if (!map.has(company)) {
            map.set(company, employee);
        } else {
            let temp = map.get(company).split(" ");
            if (temp.indexOf(employee) === -1) {
                map.set(company, map.get(company) + " " + employee);
            }
        }
    }
    for (let [key, value] of map) {
        console.log(key);
        value = value.split(" ");
        if (value.length > 1) {
            for (let employee of value) {
                console.log(`-- ${employee}`);
            }
        } else {
            console.log(`-- ${value[0]}`);
        }
    }
}

companyUsers([
    "SoftUni -> AA12345",
    "SoftUni -> BB12345",
    "Microsoft -> CC12345",
    "HP -> BB12345",
]);

companyUsers([
    "SoftUni -> AA12345",
    "SoftUni -> CC12344",
    "Lenovo -> XX23456",
    "SoftUni -> AA12345",
    "Movement -> DD11111",
]);
