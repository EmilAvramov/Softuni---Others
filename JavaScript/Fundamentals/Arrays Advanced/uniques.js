function uniques(arr) {
    let newArr = [...new Set(arr)]
    console.log(newArr.join(" "))
}

uniques([7, 8, 9, 7, 2, 3, 4, 1, 2])
uniques([20, 8, 12, 13, 4, 4, 8, 5])