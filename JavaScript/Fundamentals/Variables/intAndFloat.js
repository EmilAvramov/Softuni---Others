function numberTypes(num1, num2, num3) {
  let result = num1 + num2 + num3;
  let type = "";
  result % 1 === 0 ? (type = "Integer") : (type = "Float");
  console.log(`${result} - ${type}`);
}

numberTypes(9, 100, 1.1);
