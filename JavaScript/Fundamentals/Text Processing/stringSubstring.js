function substring(word = "", string = "") {
    let lowerWord = word.toLowerCase();
    let lowerString = string.toLowerCase();
    if (lowerString.indexOf(lowerWord) === -1) {
        console.log(`${word} not found!`);
    } else {
        console.log(`${word}`);
    }
}

substring("javascript", "JavaScript is the best programming language");
substring("python", "JavaScript is the best programming language");
