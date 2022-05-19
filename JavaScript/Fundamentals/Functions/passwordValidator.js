function pwValidate(string) {
    const isLength = (str) => {
        return str.length >= 6 && str.length <= 10;
    };
    function isAlphaNumeric(str) {
        var code;

        for (i = 0; i < str.length; i++) {
            code = str.charCodeAt(i);
            if (
                !(code > 47 && code < 58) &&
                !(code > 64 && code < 91) &&
                !(code > 96 && code < 123)
            ) {
                return false;
            }
        }
        return true;
    }
    function hasTwoDigits(str) {
        var code;
        var counter = 0;

        for (i = 0; i < str.length; i++) {
            code = str.charCodeAt(i);
            if (code > 47 && code < 58) {
                counter += 1;
            }
        }
        return counter >= 2;
    }
    if (isLength(string) && isAlphaNumeric(string) && hasTwoDigits(string)) {
        console.log("Password is valid");
    } else {
        if (!isLength(string)) {
            console.log("Password must be between 6 and 10 characters");
        }
        if (!isAlphaNumeric(string)) {
            console.log("Password must consist only of letters and digits");
        }
        if (!hasTwoDigits(string)) {
            console.log("Password must have at least 2 digits");
        }
    }
}

pwValidate("logIn");
pwValidate("MyPass123");
pwValidate("Pa$s$s");
