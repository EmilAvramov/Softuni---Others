function solve() {
    var text = document.getElementById("text").value;
    var type = document.getElementById("naming-convention").value;
    let words = text.split(" ");
    let newString = "";
    if (type === "Camel Case") {
        for (let word of words) {
            newString === ""
                ? (newString += word.toLowerCase())
                : (newString +=
                      word[0].toUpperCase() +
                      word.slice(1, word.length).toLowerCase());
        }
        document.getElementById("result").innerHTML = newString;
    } else if (type === "Pascal Case") {
        for (let word of words) {
            newString +=
                word[0].toUpperCase() +
                word.slice(1, word.length).toLowerCase();
        }
        document.getElementById("result").innerHTML = newString;
    } else {
        document.getElementById("result").innerHTML = "Error!";
    }
}
