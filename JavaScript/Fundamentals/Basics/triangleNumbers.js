function triangle(num) {
  for (let i = 1; i <= num; i++) {
    let result = "";
    for (let j = 1; j <= i; j++) {
      result += `${i} `;
    }
    console.log(result);
  }
}

triangle(5);
