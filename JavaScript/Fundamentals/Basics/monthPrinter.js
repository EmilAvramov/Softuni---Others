function months(num) {
  var months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
  ];
  if (num > 12 || num < 1) {
    console.log("Error!");
  } else {
    console.log(months[num - 1]);
  }
}
