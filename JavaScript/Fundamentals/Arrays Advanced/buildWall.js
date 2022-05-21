function wall(arr = []) {
    arr = arr.map(Number);
    let concreteYards = 0;
    const cost = 195 * 1900;
    let smallest = arr.indexOf(Math.min(...arr));
    let dayAmount = 0;
    let dayArray = []
    while (arr[smallest] < 30) {
        for (let i = 0; i < arr.length; i++) {
            if (arr[i] < 30) {
                arr[i]++;
                dayAmount += 195;
                concreteYards++;
            }
        }
        dayArray.push(dayAmount)
        dayAmount = 0;
    }
    console.log(dayArray.join(", "))
    console.log(`${concreteYards * cost} pesos`);
}

wall([17, 22, 17, 19, 17]);
console.log("--");
wall([17]);
