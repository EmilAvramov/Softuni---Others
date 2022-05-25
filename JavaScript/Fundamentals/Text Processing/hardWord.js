function letter(arr = []) {
    var letter = arr[0].split(" ");
    var words = arr[1];
    const regex = /(_+)\w/;
    for (let element of letter) {
        if (regex.test(element)) {
            for (let word of words) {
                if (element.match(regex)[0].length === word.length) {
                    if (element.length !== word.length) {
                        let mark = element.slice(
                            element.length - 1,
                            element.length
                        );
                        letter.splice(letter.indexOf(element), 1, word + mark);
                    } else {
                        letter.splice(letter.indexOf(element), 1, word);
                    }
                }
            }
        }
    }
    console.log(letter.join(" "));
}

letter([
    "Hi, grandma! I'm so ____ to write to you. ______ the winter vacation, so _______ things happened. My dad bought me a sled. Mom started a new job as a __________. My brother's ankle is ________, and now it bothers me even more. Every night Mom cooks ___ on your recipe because it is the most delicious. I hope this year Santa will _____ me a robot.",
    ["pie", "bring", "glad", "During", "amazing", "pharmacist", "sprained"],
]);
