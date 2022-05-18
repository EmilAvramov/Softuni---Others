function differences(array) {
  let sumOdd = 0;
  let sumEven = 0;
  /*
  for (let i = 0; i < array.length; i++) {
    if (array[i] % 2 === 0) {
      sumEven += array[i];
    } else {
      sumOdd += array[i];
    }
  }
  */

  for (let num of array) {
    if (num % 2 === 0) {
      sumEven += num;
    } else {
      sumOdd += num;
    }
  }
  console.log(sumEven - sumOdd);
}

differences([1, 2, 3, 4, 5, 6]);
