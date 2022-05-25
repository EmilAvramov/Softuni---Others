function asciiSum(arr = []) {
    var start, end;
    var string = arr[2];
    let sum = 0;

    if (arr[0].charCodeAt(0) > arr[1].charCodeAt(0)) {
        start = arr[1].charCodeAt(0);
        end = arr[0].charCodeAt(0);
    } else {
        start = arr[0].charCodeAt(0);
        end = arr[1].charCodeAt(0);
    }

    for (let letter of string) {
        if (letter.charCodeAt(0) > start && letter.charCodeAt(0) < end) {
            sum += letter.charCodeAt(0);
        }
    }
    
    console.log(sum);
}

asciiSum([".", "@", "dsg12gr5653feee5"]);
asciiSum(["a", "1", "jfe392$#@j24ui9ne#@$"]);
