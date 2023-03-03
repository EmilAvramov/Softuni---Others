function sumDigits(number) {
    let sum = 0
    let numToString = number.toString()
    for (let i = 0; i < numToString.length; i++) {
        sum += parseInt(numToString[i]) 
    }

    console.log(sum)
}

sumDigits(245678)