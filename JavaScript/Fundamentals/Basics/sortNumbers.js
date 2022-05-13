function sorted(num1, num2, num3) {
    let numbers = [];
    numbers.push(num1, num2, num3)
    numbers.sort().reverse()
    for (let i = 0; i < numbers.length; i++) {
        console.log(numbers[i])
    }
}

sorted(-2, 1, 3)