function sortArray(arr) {
    let sortedArray = arr.sort()

    sortedArray.forEach((name, index) => {
        console.log(`${index + 1}.${name}`);
    })
    // for (let i = 0; i < sortedArray.length; i++) {
    //     console.log(`${i+1}.${sortedArray[i]}`)
    // }
}

sortArray(["John", "Bob", "Christina", "Ema"])