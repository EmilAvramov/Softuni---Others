function increasingSubSet(arr = []) {
    let largest = Number.MIN_SAFE_INTEGER;
    let newArr = [];
    for (let number of arr) {
        if (number >= largest) {
            largest = number;
            newArr.push(number);
        }
    }
    return newArr;
}

console.log(increasingSubSet([1, 3, 8, 4, 10, 12, 3, 2, 24]));
