function sorting(arr) {
    const length = arr.length;
    let finalList = [];
    let sorted = arr.sort((a, b) => {return a - b}).reverse();
    for (let i = 0; i < length; i++) {
        if (i % 2 !== 0) {
            finalList.push(sorted.pop());
        } else {
            finalList.push(sorted.shift());
        }
    }

    console.log(finalList.join(" "));
}

sorting([1, 21, 3, 52, 69, 63, 31, 2, 18, 94]);
sorting([34, 2, 32, 45, 690, 6, 32, 7, 19, 47]);
