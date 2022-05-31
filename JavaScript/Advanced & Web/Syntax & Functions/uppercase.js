function uppercase(string) {
    let words = [];
    words.push(string.match(/\b\w+/g));
    console.log(words[0].join(", ").toUpperCase());
}

uppercase("Hi, how are you?");
uppercase("Functions in JS can be nested, i.e. hold other functions");
