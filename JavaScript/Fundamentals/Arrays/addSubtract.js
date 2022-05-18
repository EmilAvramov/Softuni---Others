function operations(arr) {
  let modifiedSum = 0;
  let originalSum = 0;
  for (let i = 0; i < arr.length; i++) {
    originalSum += arr[i];
    if (arr[i] % 2 === 0) {
      arr[i] += i;
    } else {
      arr[i] -= i;
    }
    modifiedSum += arr[i];
  }
  console.log(arr);
  console.log(originalSum);
  console.log(modifiedSum);
}

operations([5, 15, 23, 56, 35]);
