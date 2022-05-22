//@ts-check

class Media {
    /**
     * @param {any} title
     */
    constructor(title) {
        this._title = title;
        this._ratings = [];
        this._isCheckedOut = false;
    }

    get title() {
        return this._title;
    }
    get ratings() {
        return this._ratings;
    }
    get isCheckedOut() {
        return this._isCheckedOut;
    }
    set isCheckedOut(value) {
        this._isCheckedOut = value;
    }
    toggleCheckOutStatus() {
        if (this._isCheckedOut) {
            this._isCheckedOut = false;
        } else {
            this._isCheckedOut = true;
        }
    }
    getAverageRating() {
        let total = this._ratings.reduce((a, b) => a + b, 0);
        return total / this._ratings.length;
    }
    /**
     * @param {number} rating
     */
    addRating(rating) {
        if (rating > 0 && rating < 6) {
            this._ratings.push(rating);
        } else {
            console.log("Please use the 1-5 scale");
        }
    }
}

class Book extends Media {
    /**
     * @param {string} title
     * @param {string} author
     * @param {number} pages
     */
    constructor(title, author, pages) {
        super(title);
        this._author = author;
        this._pages = pages;
    }

    get author() {
        return this._author;
    }
    get pages() {
        return this._pages;
    }
}

class Movie extends Media {
    /**
     * @param {string} title
     * @param {string} director
     * @param {number} runTime
     */
    constructor(title, director, runTime) {
        super(title);
        this._director = director;
        this._runTime = runTime;
    }
    get director() {
        return this._director;
    }
    get runTime() {
        return this._runTime;
    }
}

class CD extends Media {
    /**
     * @param {any} title
     * @param {any} artist
     * @param {any} songs
     */
    constructor(title, artist, songs) {
        super(title);
        this._artist = artist;
        this._songs = songs;
    }
    get artist() {
        return this._artist;
    }
    get songs() {
        return this._songs;
    }
}

const historyOfEverything = new Book(
    "A Short History of Nearly Everything",
    "Bill Bryson",
    544
);
console.log(historyOfEverything);
historyOfEverything.toggleCheckOutStatus();
console.log(historyOfEverything.isCheckedOut);
historyOfEverything.addRating(4);
historyOfEverything.addRating(5);
historyOfEverything.addRating(5);
console.log(historyOfEverything.getAverageRating());

const speed = new Movie("Speed", "Jan de Bont", 116);
speed.toggleCheckOutStatus();
console.log(speed.isCheckedOut);
speed.addRating(5);
speed.addRating(1);
speed.addRating(1);
console.log(speed.getAverageRating());

const someSongs = new CD("I am a burrito", "Your Kitchedn", [
    "Taco",
    "You hungry?",
    "Burrito",
]);
console.log(someSongs);
someSongs.addRating(6);
