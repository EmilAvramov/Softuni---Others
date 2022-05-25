function search(text = "", word) {
    text = text.split(" ");
    let count = 0;
    for (let element of text) {
        if (element === word) {
            count++;
        }
    }
    console.log(count);
}

search("This is a word and it also is a sentence", "is");
search(
    "softuni is great place for learning new programming languages",
    "softuni"
);
