function matrixBiggest(arr = []) {
    let max = Number.MIN_SAFE_INTEGER;
    arr.forEach((subArr) => {
        let current = Math.max(...subArr);
        if (current > max) {
            max = current;
        }
    });
    return max;
}

console.log(
    matrixBiggest([
        [3, 5, 7, 12],
        [-1, 4, 33, 2],
        [8, 3, 0, 4],
    ])
);
console.log(
    matrixBiggest([
        [20, 50, 10],
        [8, 33, 145],
    ])
);
