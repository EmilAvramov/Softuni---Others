function identical(array1, array2) {
  let arraySum = 0;

  for (let i = 0; i < array1.length; i++) {
    arraySum += Number(array1[i]);
    if (array1[i] !== array2[i]) {
      console.log(`Arrays are not identical. Found difference at ${i} index`);
      return;
    }
  }

  console.log(`Arrays are identical. Sum: ${arraySum}`);
}

identical(["10", "20", "30"], ["10", "20", "30"]);
identical(["1"], ["10"]);
identical(["1", "2", "3", "4", "5"], ["1", "2", "4", "4", "5"]);
