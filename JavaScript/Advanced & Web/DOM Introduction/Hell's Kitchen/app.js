function solve() {
    document.querySelector("#btnSend").addEventListener("click", onClick);

    function onClick() {
        var input = JSON.parse(
            document.querySelector("#inputs textarea").value
        );
        var outputAverage = document.querySelector("#bestRestaurant>p");
        var outputWorkers = document.querySelector("#workers>p");
        let winner = findBest(input);
        outputAverage.textContent = bestRestaurant(winner);
        outputWorkers.textContent = bestWorkers(winner);
    }
    function bestRestaurant(obj = {}) {
        return `Name: ${
            obj.bestRestaurant
        } Average Salary: ${obj.bestAverage.toFixed(
            2
        )} Best Salary: ${obj.bestSalary.toFixed(2)}`;
    }

    function bestWorkers(obj = {}) {
        return Object.entries(obj.bestWorkers)
            .map(
                (property) => `Name: ${property[0]} With Salary: ${property[1]}`
            )
            .join(" ");
    }

    function findBest(data = []) {
        var bestRest = {
            bestRestaurant: "",
            bestAverage: Number.MIN_SAFE_INTEGER,
            bestSalary: Number.MIN_SAFE_INTEGER,
            bestWorkers: {},
        };
        data.forEach((line) => {
            let restaurant = line.split(" - ")[0];
            let workerInfo = line
                .split(" - ")[1]
                .split(", ")
                .sort((a, b) => b.split(" ")[1] - a.split(" ")[1]);
            let workerObj = {};

            for (let i = 0; i < workerInfo.length; i++) {
                let name = workerInfo[i].split(" ")[0];
                let salary = Number(workerInfo[i].split(" ")[1]);
                workerObj[name] = salary;
            }

            let average =
                Object.values(workerObj).reduce((a, b) => a + b) /
                workerInfo.length;

            if (average > bestRest.bestAverage) {
                bestRest.bestAverage = average;
                bestRest.bestRestaurant = restaurant;
                bestRest.bestSalary = Math.max(...Object.values(workerObj));
                bestRest.bestWorkers = workerObj;
            }
        });
        return bestRest;
    }
}
