function signCheck(num1, num2, num3) {
  const isNeg = (num) => {
    return num < 0;
  };
  let negatives = 0;
  if (isNeg(num1)) {
    negatives += 1;
  }
  if (isNeg(num2)) {
    negatives += 1;
  }
  if (isNeg(num3)) {
    negatives += 1;
  }

  if (negatives === 1 || negatives === 3) {
    console.log("Negative");
  } else {
    console.log("Positive");
  }
}

signCheck(5, 12, -15);
signCheck(-6, -12, 14);
