function pascalFormat(string = "") {
    let words = [];
    let word = "";
    for (let i = 0; i < string.length; i++) {
        if (string[i] === string[i].toUpperCase() && word === "") {
            word += string[i];
        } else if (string[i] !== string[i].toUpperCase()) {
            word += string[i];
        } else if (string[i] === string[i].toUpperCase() && word !== "") {
            words.push(word);
            word = "";
            word += string[i];
        }
    }
    words.push(word);
    console.log(words.join(", "));
}

pascalFormat("SplitMeIfYouCanHaHaYouCantOrYouCan");
pascalFormat("HoldTheDoor");
pascalFormat("ThisIsSoAnnoyingToDo");
