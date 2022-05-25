function replaceChars(word = "") {
    let newWord = ""
    for (let i = 0; i < word.length; i++) {
        if (word[i] !== word[i + 1]) {
            newWord += word[i]
        }
    }
    console.log(newWord);
}

replaceChars("aaaaabbbbbcdddeeeedssaa");
replaceChars('qqqwerqwecccwd')