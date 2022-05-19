function rotate(arr) {
  const rotations = Number(arr.pop());
  let trueArr = arr;
  for (let i = 1; i <= rotations; i++) {
    let temp = trueArr.pop();
    trueArr.splice(0, 0, temp);
  }
  console.log(trueArr.join(" "));
}

rotate(["1", "2", "3", "4", "2"]);
rotate(["Banana", "Orange", "Coconut", "Apple", "15"]);
