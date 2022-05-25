function passwords(arr = []) {
    var string = arr[0] + arr[1];
    const symbols = arr[2];
    let newString = "";
    let index = 0;
    var vowels = ["a", "o", "u", "i", "e"];
    for (let i = 0; i < string.length; i++) {
        if (vowels.includes(string[i])) {
            newString += symbols[index].toUpperCase();
            index++;
            if (index === symbols.length) {
                index = 0;
            }
        } else {
            newString += string[i];
        }
    }
    console.log(
        `Your generated password is ${newString.split("").reverse().join("")}`
    );
}

passwords(["ilovepizza", "ihatevegetables", "orange"]);
passwords(["easymoneyeazylife", "atleasttencharacters", "absolute"]);
passwords(["areyousureaboutthisone", "notquitebutitrustyou", "disturbed"]);
