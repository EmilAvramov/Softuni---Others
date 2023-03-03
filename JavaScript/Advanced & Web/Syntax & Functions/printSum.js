function printSum(first, last) {
    let row = []
    let sum = 0

    for (let i = first; i <= last; i++) {
        sum += i
        row.push(i)
    }

    console.log(row.join(' '))
    console.log(`Sum: ${sum}`)
}

printSum(5, 10)