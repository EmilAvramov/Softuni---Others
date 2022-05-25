function addSub(num1, num2, num3) {
  let add = (num1, num2) => {
    return num1 + num2;
  };
  let subtract = (func, num3) => {
    return func - num3;
  };
  console.log(subtract(add(num1, num2), num3));
}

addSub(23, 6, 10);
addSub(1, 17, 30);
