function condense(array) {
  while (array.length > 1) {
    let condensed = Array(array.length - 1);
    for (let i = 0; i < array.length - 1; i++) {
      condensed[i] = Number(array[i] + array[i + 1]);
    }
    array = condensed;
  }
  console.log(array[0]);
}

condense([2, 10, 3]);
condense([5, 0, 4, 1, 2]);
