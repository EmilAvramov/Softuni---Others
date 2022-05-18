function sumEven(array) {
  let sumTotal = 0;
  for (let i = 0; i < array.length; i++) {
    let number = parseInt(array[i]);
    if (number % 2 === 0) {
      sumTotal += parseInt(array[i]);
    }
  }
  console.log(sumTotal);
}

sumEven(["1", "2", "3", "4", "5", "6"]);
