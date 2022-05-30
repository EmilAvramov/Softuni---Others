function focused() {
    var mainDiv = document.querySelector("div");
    Array.from(mainDiv.getElementsByTagName("input")).forEach((element) => {
        element.addEventListener("focus", focus);
        element.addEventListener("blur", blur);
    });

    function focus(event) {
        event.target.parentNode.classList.add("focused");
    }

    function blur(event) {
        event.target.parentNode.classList.remove("focused");
    }
}
