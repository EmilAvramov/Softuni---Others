function studentGrades(data) {
    var map = new Map();

    data = data.sort((a, b) => {
        return a.split(" ")[0] > b.split(" ")[0] ? 1 : -1;
    });

    for (let line of data) {
        let name, grades;
        [name, ...grades] = line.split(" ");
        
        if (!map.has(name)) {
            map.set(name, grades);
        } else {
            for (let grade of map.get(name)) {
                grades.push(grade);
            }
            map.set(name, grades);
        }
    }

    for (let [key, value] of map) {
        map.set(
            key,
            value.map(Number).reduce((a, b) => a + b, 0) / value.length
        );
    }
    for (const [key, value] of map) {
        console.log(`${key}: ${value.toFixed(2)}`);
    }
}

studentGrades(["Lilly 4 6 6 5", "Tim 5 6", "Tammy 2 4 3", "Tim 6 6"]);
studentGrades(["Steven 3 5 6 4", "George 4 6", "Tammy 2 5 3", "Steven 6 3"]);
