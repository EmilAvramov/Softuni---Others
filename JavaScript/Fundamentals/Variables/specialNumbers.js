function specials(num) {
  const check = [5, 7, 11];
  for (let i = 1; i <= num; i++) {
    var sum = 0;
    var number = i;
    while (number) {
      sum += number % 10;
      number = Math.floor(number / 10);
    }
    if (check.includes(sum)) {
      console.log(`${i} -> True`);
    } else {
      console.log(`${i} -> False`);
    }
  }
}

specials(15);
