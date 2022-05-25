function modernTimes(string = "") {
    string = string.split(" ");
    let nextFlag = false;
    for (let i = 0; i < string.length; i++) {
        if (string[i].startsWith("#") && string[i].length > 1) {
            for (let j = 1; j < string[i].length; j++) {
                let check = string[i][j].toUpperCase();
                if (check.charCodeAt(0) < 65 || check.charCodeAt(0) > 90) {
                    nextFlag = true;
                }
            }
            if (nextFlag === false) {
                console.log(string[i].substring(1, string[i].length));
            }
            nextFlag = false;
        }
    }
}

modernTimes("Nowadays everyone uses # to tag a #special word in #socialMedia");
modernTimes(
    "The symbol # is known #variously in English-speaking #regi@ons as the #number sign"
);
