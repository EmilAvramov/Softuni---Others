function biggestHalf(arr = []) {
    arr = arr.sort((a, b) => {
        return a > b ? 1 : -1;
    });
    if (arr.length % 2 === 0) {
        return arr.slice(arr.length / 2, arr.length);
    } else {
        return arr.slice(Math.floor(arr.length / 2), arr.length);
    }
}

biggestHalf([4, 7, 2, 5]);
biggestHalf([3, 19, 14, 7, 2, 19, 6]);
