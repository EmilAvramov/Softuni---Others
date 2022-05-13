function numbers(start, end) {
    var numbers = []
    var sum = 0
    for (let i=start; i<=end; i++){
        numbers.push(i)
        sum += i
    }
    console.log(numbers.join(" "))
    console.log(`Sum: ${sum}`)
}

numbers(5, 10)