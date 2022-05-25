function numMod(num) {
    function findAverage(num) {
        let digits = num.toString().split("").map(Number);
        let sum = 0;
        digits.forEach((element) => {
            sum += element;
        });
        let average = sum / digits.length;
        return average < 5;
    }

    while (findAverage(num)) {
        num = num.toString() + 9;
        num = Number(num);
    }

    console.log(num);
}

numMod(101);
numMod(5835);
