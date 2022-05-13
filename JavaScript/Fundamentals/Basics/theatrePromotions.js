function theatre(type, age) {
  var data = {
    Weekday: {
      kid: 12,
      adult: 18,
      elder: 12,
    },
    Weekend: {
      kid: 15,
      adult: 20,
      elder: 15,
    },
    Holiday: {
      kid: 5,
      adult: 12,
      elder: 10,
    },
  };
  for (let key in data) {
    if (type === key) {
      if (0 <= age && age <= 18) {
        console.log(`${data[key].kid}$`);
      } else if (18 < age && age <= 64) {
        console.log(`${data[key].adult}$`);
      } else if (64 < age && age <= 122) {
        console.log(`${data[key].elder}$`);
      } else {
        console.log("Error!");
      }
    }
  }
}
