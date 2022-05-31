function melrah(arr = []) {
    function sliceString(data, match, pat) {
        data = data.slice(0, match) + data.slice(match + pat.length);
        return data;
    }
    function slicePatter(pat) {
        pat = pat.slice(0, pat.length / 2) + pat.slice(pat.length / 2 + 1);
        return pat;
    }
    var text = arr.shift();
    var pattern = arr.shift();

    while (pattern.length > 0) {
        let firstMatch = text.indexOf(pattern);
        let lastMatch = text.lastIndexOf(pattern);
        if (firstMatch > -1 && lastMatch > -1 && firstMatch !== lastMatch) {
            text = sliceString(text, firstMatch, pattern);
            lastMatch = text.lastIndexOf(pattern);
            text = sliceString(text, lastMatch, pattern);
            pattern = slicePatter(pattern);
            console.log("Shaked it.");
        } else {
            break;
        }
    }
    console.log("No shake.");
    console.log(text);
}

melrah(["astalavista baby", "sta"]);
