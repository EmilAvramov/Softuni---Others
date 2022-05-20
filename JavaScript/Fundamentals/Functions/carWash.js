function carWash(arr) {
    let cleanliness = 0;
    arr.forEach((element) => {
        switch (element) {
            case "soap":
                cleanliness += 10;
                break;
            case "water":
                cleanliness += cleanliness * 0.2;
                break;
            case "vacuum cleaner":
                cleanliness += cleanliness * 0.25;
                break;
            case "mud":
                cleanliness -= cleanliness * 0.1;
        }
    });
    console.log(`The car is ${cleanliness.toFixed(2)}% clean.`);
}


carWash(['soap', 'soap', 'vacuum cleaner', 'mud', 'soap', 'water'])
carWash(["soap", "water", "mud", "mud", "water", "mud", "vacuum cleaner"])