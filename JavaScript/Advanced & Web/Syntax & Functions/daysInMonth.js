function monthDays(month, year) {
    console.log(new Date(year, month, 0).getDate());
}

monthDays(1, 2012);
