function oddEven(num) {
    const numbers = num.toString().split("").map(Number);
    let oddSum = 0;
    let evenSum = 0;
    numbers.forEach((element) => {
        if (element % 2 == 0) {
            evenSum += element;
        } else {
            oddSum += element;
        }
    });
    console.log(`Odd sum = ${oddSum}, Even sum = ${evenSum}`);
}

oddEven(1000435);
