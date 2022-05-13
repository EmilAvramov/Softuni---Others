function roundNumber(num, precision) {
  if (precision > 15) {
    console.log(parseFloat(num.toFixed(15)));
  } else {
    console.log(parseFloat(num.toFixed(precision)));
  }
}
