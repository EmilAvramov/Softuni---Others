function oddEven(number) {
    let string = number.toString()
    let even = 0
    let odd = 0

    for (let i = 0; i < string.length; i++) {
        if (string[i] % 2 === 0) {
            even += parseInt(string[i])
        } else {
            odd += parseInt(string[i])
        }
    }

    console.log(`Odd sum = ${odd}, Even sum = ${even}`)
}

oddEven(1000435)
oddEven(3495892137259234)