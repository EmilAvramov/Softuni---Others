function filtering(arr) {
  let max = null;
  function largest(num) {
    if (max === null) {
      max = num;
      return num;
    } else if (num >= max) {
      max = num;
      return num;
    }
  }
  let newArr = arr.filter(largest);
  console.log(newArr.join(" "));
}

filtering([1, 3, 8, 4, 10, 12, 3, 2, 24]);
filtering([1, 2, 3, 4]);
filtering([20, 3, 2, 15, 6, 1]);
filtering([-2, 0, -2]);
