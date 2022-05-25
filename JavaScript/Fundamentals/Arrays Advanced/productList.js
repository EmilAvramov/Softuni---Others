function productList(arr) {
    arr = arr.sort();
    for (let i = 0; i < arr.length; i++) {
        console.log(`${i + 1}.${arr[i]}`);
    }
}

productList(["Potatoes", "Tomatoes", "Onions", "Apples"]);
productList(["Watermelon", "Banana", "Apples"]);
