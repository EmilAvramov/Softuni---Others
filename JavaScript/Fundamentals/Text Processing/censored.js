function censored(text = "", censored) {
    while (text.includes(censored)) {
        text = text.replace(censored, length(censored));
    }
    console.log(text)

    function length(word) {
        let replace = "";
        for (let i = 0; i < word.length; i++) {
            replace += "*";
        }
        return replace;
    }
}

censored("A small sentence with some words", "small");
