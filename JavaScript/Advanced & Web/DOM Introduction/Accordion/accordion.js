function toggle() {
    var text = document.getElementById("extra");
    var button = document.querySelector("body div span")
    if (text.style.display === "none") {
        text.style.display = "block";
        button.innerHTML = "Less";
    } else {
        text.style.display = "none";
        button.innerHTML = "More";
    }
}
