function detonate(arr1, arr2) {
    let bomb = Number(arr2[0]);
    let range = Number(arr2[1]);
    while (arr1.includes(bomb)) {
        let index = arr1.indexOf(bomb);
        let elementsToRemove = range * 2 + 1;
        let startIndex = index - range;

        if (startIndex < 0) {
            elementsToRemove += startIndex;
            startIndex = 0;
        }
        arr1.splice(startIndex, elementsToRemove);
        
    }
    console.log(arr1.reduce((a, partial) => a + partial, 0));
}

detonate([1, 2, 2, 4, 2, 2, 2, 9], [4, 2]);
detonate([1, 4, 4, 2, 8, 9, 1], [9, 3]);
detonate([1, 7, 7, 1, 2, 3], [7, 1]);
detonate([1, 1, 2, 1, 1, 1, 2, 1, 1, 1], [2, 1]);
