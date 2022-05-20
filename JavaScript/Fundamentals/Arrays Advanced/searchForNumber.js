function search(arr1, arr2) {
    let range = arr2[0];
    let remove = arr2[1];
    let count = 0;
    const search = arr2[2];
    arr1 = arr1.slice(0, range);
    arr1.splice(0, remove);
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] === search) {
            count += 1;
        }
    }
    console.log(`Number ${search} occurs ${count} times.`);
}

search([5, 2, 3, 4, 1, 6], [5, 2, 3]);
