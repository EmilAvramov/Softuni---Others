function rotations(arr, times) {
  for (let i = 1; i <= times; i++) {
    let temp = arr.shift();
    arr.push(temp);
  }
  console.log(arr.join(" "));
}

rotations([51, 47, 32, 61, 21], 2);
