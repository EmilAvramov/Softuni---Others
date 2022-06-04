function createBook(title, author, read = false) {
    return {
        title: title,
        author: author,
        read: read,
        getDescription() {
            console.log(
                `${this.title} was written by ${this.author}. I ${
                    this.read ? "have" : "have not"
                } read it.`
            );
        },
        readBook() {
            this.read = true;
        },
    };
}

const beloved = createBook("Beloved", "Toni Morrison");
console.log(beloved);
/*
{
    title: 'Beloved',
    author: 'Toni Morrison',
    read: false,
    getDescription: [Function: getDescription],
    readBook: [Function: readBook]
}
*/

// call the `.readBook()` method
beloved.readBook(); // read is updated to true

// modifies the property directly
beloved.title = "I can change the property.";
