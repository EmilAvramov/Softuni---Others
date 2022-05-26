function arrayEven(arr = []) {
    arr = arr.filter((element) => arr.indexOf(element) % 2 === 0);
    console.log(arr.join(" "));
}

arrayEven(["20", "30", "40", "50", "60"]);
