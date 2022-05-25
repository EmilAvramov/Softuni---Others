function longestSeq(arr) {
  let count = 0;
  let sequence = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] !== arr[i + 1]) {
      count = 0;
    } else {
      count += 1;
      if (count + 1 > sequence.length) {
        sequence = [];
        for (let j = 0; j < count + 1; j++) {
          sequence.push(arr[i]);
        }
      }
    }
  }
  console.log(sequence.join(" "));
}

longestSeq([2, 1, 1, 2, 3, 3, 2, 2, 2, 1]);
longestSeq([1, 1, 1, 2, 3, 1, 3, 3]);
longestSeq([4, 4, 4, 4]);
longestSeq([0, 1, 1, 5, 2, 2, 6, 3, 3]);
