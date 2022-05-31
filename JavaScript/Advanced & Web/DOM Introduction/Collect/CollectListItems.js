function extractText() {
    var data = []
    var target = document.getElementById("items")
    for (i = 1; i <= target.childElementCount * 2; i+=2) {
        data.push(target.childNodes[i].innerHTML)
    }
    document.getElementById("result").innerHTML = data.join("\n")
}