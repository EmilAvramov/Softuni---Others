function smallest(arr) {
    let sortedArr = arr.sort((a, b) => {
        return a - b;
    });
    console.log(sortedArr.shift() + " " + sortedArr.shift());
}

smallest([30, 15, 50, 5]);
