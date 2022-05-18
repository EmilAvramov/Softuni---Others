function evenSums(arr) {
  let leftSum = 0;
  let rightSum = 0;
  for (let i = 0; i < arr.length; i++) {
    for (let j = 0; j < i; j++) {
      leftSum += arr[j];
    }
    for (let j = i + 1; j < arr.length; j++) {
      rightSum += arr[j];
    }
    if (leftSum === rightSum) {
      console.log(i);
      return;
    } else if (leftSum === 0 && rightSum === 0) {
      console.log(0);
      return;
    }
    leftSum = 0;
    rightSum = 0;
  }
  console.log("no");
}

evenSums([1, 2, 3, 3]);
evenSums([1, 2]);
evenSums([1]);
evenSums([10, 5, 5, 99, 3, 4, 2, 5, 1, 1, 4]);