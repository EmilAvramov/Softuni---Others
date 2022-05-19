function addRemove(arr) {
  let numArr = [];
  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "add") {
      numArr.push(i + 1);
    } else {
      numArr.pop();
    }
  }
  if (numArr.length > 0) {
    console.log(numArr.join(" "));
  } else {
    console.log("Empty");
  }
}

addRemove(["add", "add", "add", "add"]);
addRemove(["add", "add", "remove", "add", "add"]);
addRemove(["remove", "remove", "remove"]);
