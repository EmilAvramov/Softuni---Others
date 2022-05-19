function calculator(num1, num2, operator) {
  const operations = {
    multiply: function (x, y) {
      return x * y;
    },
    divide: function (x, y) {
      return x / y;
    },
    add: function (x, y) {
      return x + y;
    },
    subtract: function (x, y) {
      return x - y;
    },
  };
  console.log(operations[operator](num1, num2));
}

calculator(5, 5, "multiply");
calculator(40, 8, "divide");
