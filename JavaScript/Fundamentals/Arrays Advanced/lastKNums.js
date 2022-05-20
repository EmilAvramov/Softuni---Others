function likeFibonacci(length, lastSum) {
    let numbers = [1];
    let tempNum = 0;
    let tempArr = [];
    for (let i = 1; i < length; i++) {
        if (numbers.length >= lastSum) {
            tempArr = numbers.slice(-lastSum);
            tempArr.forEach((element) => {
                tempNum += element;
            });
            numbers.push(tempNum);
            tempNum = 0;
        } else {
            numbers.push(i);
        }
    }
    console.log(numbers.join(" "));
}

likeFibonacci(6, 3);
likeFibonacci(8, 2);
