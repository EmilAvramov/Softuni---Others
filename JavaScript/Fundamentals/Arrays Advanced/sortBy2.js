function advancedSort(arr) {
    arr = arr.sort((a, b) => a.length - b.length || a.localeCompare(b));
    console.log(arr.join("\n"));
}

advancedSort(["alpha", "beta", "gamma"]);
advancedSort(["Isacc", "Theodor", "Jack", "Harrison", "George"]);
console.log("------");
advancedSort(["test", "Deny", "omen", "Default"]);
