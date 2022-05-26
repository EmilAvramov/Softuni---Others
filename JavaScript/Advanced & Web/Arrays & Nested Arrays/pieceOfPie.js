function pie(arr = [], target1 = "", target2 = "") {
    return arr.slice(arr.indexOf(target1), arr.indexOf(target2) + 1);
}

console.log(
    pie(
        [
            "Pumpkin Pie",
            "Key Lime Pie",
            "Cherry Pie",
            "Lemon Meringue Pie",
            "Sugar Cream Pie",
        ],
        "Key Lime Pie",
        "Lemon Meringue Pie"
    )
);
