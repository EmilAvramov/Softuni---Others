function kNumbers(arr) {
    let k, newArr, first, last;
    [k, ...newArr] = arr;
    first = newArr.slice(0, k);
    last = newArr.slice(newArr.length - k, newArr.length);
    console.log(first.join(" "));
    console.log(last.join(" "));
}

kNumbers([2, 7, 8, 9]);
kNumbers([3, 6, 7, 8, 9]);
