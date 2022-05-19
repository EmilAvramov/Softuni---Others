function matrices(arr) {
  let sumAbs = 0;
  let sumCurrent = 0;
  let magic = true;
  let transposed = [];

  for (let i = 0; i < arr.length; i++) {
    // Check row in sequence
    sumCurrent = arr[i].reduce((partial, a) => partial + a, 0);
    if (sumAbs === 0) {
      sumAbs = sumCurrent;
    } else if (sumAbs !== sumCurrent) {
      magic = false;
      break;
    }
    sumCurrent = 0;
    // Transpose matrix and check row in sequence
    transposed = arr.map((x) => x[i]);
    sumCurrent = transposed.reduce((partial, a) => partial + a, 0);
    if (sumAbs !== sumCurrent) {
      magic = false;
      break;
    }
    sumCurrent = 0;
  }

  console.log(magic);
}

matrices([
  [4, 5, 6],
  [6, 5, 4],
  [5, 5, 5],
]);

matrices([
  [11, 32, 45],
  [21, 0, 1],
  [21, 1, 1],
]);

matrices([
  [1, 0, 0],
  [0, 0, 1],
  [0, 1, 0],
]);
