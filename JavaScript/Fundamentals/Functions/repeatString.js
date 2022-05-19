function repeat(str, times) {
  let newStr = "";
  for (let i = 0; i < times; i++) {
    newStr += str;
  }
  console.log(newStr);
}

repeat("abc", 3)