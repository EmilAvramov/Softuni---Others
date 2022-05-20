function oddNum(arr) {
    let newArr = [];
    for (let i = 0; i < arr.length; i++) {
        if (i % 2 !== 0) {
            newArr.push(arr[i] * 2);
        }
    }
    newArr = newArr.reverse();
    console.log(newArr.join(" "));
}

oddNum([10, 15, 20, 25]);
oddNum([3, 0, 10, 4, 7, 3]);
