function spice(resources) {
  const dayDrop = 10;
  const workers = 26;
  let days = 0;
  let totalSpice = 0;
  while (resources >= 100) {
    totalSpice += resources;
    totalSpice -= workers;
    days += 1;
    resources -= dayDrop;
  }
  if (totalSpice >= workers) {
    totalSpice -= workers;
  } else {
    totalSpice = 0;
  }
  console.log(days);
  console.log(totalSpice);
}

spice(450);
