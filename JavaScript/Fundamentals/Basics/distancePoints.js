function distance(x1, y1, x2, y2) {
  let calculated = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));
  console.log(calculated);
}

distance(2, 4, 5, 0);
