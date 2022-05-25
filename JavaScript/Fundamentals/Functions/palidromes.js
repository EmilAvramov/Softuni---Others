function palindromes(arr) {
    const check = (num) => {
        return num === Number(num.toString().split("").reverse().join(""));
    };
    arr.forEach((element) => {
        check(element) ? console.log("true") : console.log("false");
    });
}

palindromes([123, 323, 421, 121]);
palindromes([32,2,232,1010])