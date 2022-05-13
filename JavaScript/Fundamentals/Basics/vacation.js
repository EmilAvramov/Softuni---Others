function vacation(numPeople, groupType, weekDay) {
  let result = 0;
  var allTypes = {
    Students: {
      Friday: 8.45,
      Saturday: 9.8,
      Sunday: 10.46,
    },
    Business: {
      Friday: 10.9,
      Saturday: 15.6,
      Sunday: 16,
    },
    Regular: {
      Friday: 15,
      Saturday: 20,
      Sunday: 22.5,
    },
  };
  for (let key in allTypes) {
    if (key === groupType) {
      if (key === "Students") {
        if (numPeople >= 30) {
          result = allTypes[key][weekDay] * numPeople * 0.85;
        } else {
          result = allTypes[key][weekDay] * numPeople;
        }
      } else if (key === "Business") {
        if (numPeople >= 100) {
          result = allTypes[key][weekDay] * (numPeople - 10);
        } else {
          result = allTypes[key][weekDay] * numPeople;
        }
      } else if (key === "Regular"){
        if (numPeople >= 10 && numPeople <= 20) {
          result = (allTypes[key][weekDay] * numPeople) * 0.95;
        } else {
          result = allTypes[key][weekDay] * numPeople;
        }
      }
    }
  }
  console.log(`Total price: ${result.toFixed(2)}`);
}

vacation(30, "Students", "Sunday");
