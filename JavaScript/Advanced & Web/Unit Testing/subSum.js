function subSum(arr = [], start = 0, end = 0) {
    try {
        if (!Array.isArray(arr)) {
            throw NaN
        }
        if (start < 0) {
            start = 0;
        }
        if (end >= arr.length) {
            end = arr.length - 1;
        }
        let sum = 0;
        for (let i = start; i < end + 1; i++) {
            if (typeof arr[i] !== "number") {
                throw NaN;
            } else {
                sum += arr[i];
            }
        }
        return sum;
    } catch (e) {
        return e;
    }
}

console.log(subSum([10, 20, 30, 40, 50, 60], 3, 300));
console.log(subSum([1.1, 2.2, 3.3, 4.4, 5.5], -3, 1));
console.log(subSum([10, 'twenty', 30, 40], 0, 2));
