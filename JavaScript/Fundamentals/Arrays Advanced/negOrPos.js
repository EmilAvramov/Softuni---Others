function sortingAll(arr) {
    let newArr = [];
    arr.forEach((element) => {
        if (element < 0) {
            newArr.unshift(element);
        } else {
            newArr.push(element);
        }
    });
    console.log(newArr.join("\n"));
}

sortingAll(["7", "-2", "8", "9"]);
sortingAll(["3", "-2", "0", "-1"]);
