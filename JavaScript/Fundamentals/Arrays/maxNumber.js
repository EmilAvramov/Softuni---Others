function maxRight(arr) {
  let flag = true;
  let newArr = [];
  for (let i = 0; i < arr.length; i++) {
    for (let j = i + 1; j < arr.length + 1; j++) {
      if (arr[i] <= arr[j]) {
        flag = false;
        break;
      }
    }
    if (flag) {
      newArr.push(arr[i]);
    }
    flag = true;
  }
  console.log(newArr.join(" "));
}

maxRight([1, 4, 3, 2]);
maxRight([14, 24, 3, 19, 15, 17]);
maxRight([41, 41, 34, 20]);
