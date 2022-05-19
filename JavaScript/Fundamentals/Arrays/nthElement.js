function nthStep(arr) {
  let step = Number(arr.pop());
  let trueArr = arr;
  let newArr = [];
  for (let i = 0; i < trueArr.length; i += step) {
    newArr.push(trueArr[i]);
  }
  console.log(newArr.join(" "));
}

nthStep(["5", "20", "31", "4", "20", "2"]);
nthStep(["dsa", "asd", "test", "test", "2"]);
