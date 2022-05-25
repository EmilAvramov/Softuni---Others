function weekDay(dayNum) {
  const days = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
  ];
  if (dayNum > days.length) {
    console.log("Invalid day!");
  } else {
    console.log(days[dayNum - 1]);
  }
}

weekDay(3);
