function reversal(number, array) {
  var revArray = array.slice(0, number).reverse();
  console.log(revArray.join(" "));
}

reversal(3, [10, 20, 30, 40, 50]);
