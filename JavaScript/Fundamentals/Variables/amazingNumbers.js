function amazing(number) {
  var serialize = number.toString();
  let result = 0;
  for (let i = 0; i < serialize.length; i++) {
    result += ~~serialize[i];
  }
  if (result.toString().indexOf("9") > -1) {
    console.log(`${number} Amazing? True`);
  } else {
    console.log(`${number} Amazing? False`);
  }
}
amazing(1233);
amazing(999);
