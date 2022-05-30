function lockedProfile() {
    let buttons = [...document.querySelectorAll("button")];
    buttons.forEach((button) => button.addEventListener("click", addEvent));

    function addEvent(event) {
        if (event.target.parentNode.children[4].checked === true) {
            if (event.target.textContent === "Show more") {
                event.target.parentNode.children[9].style.display = "block";
                event.target.textContent = "Hide it";
            } else {
                event.target.parentNode.children[9].style.display = "none";
                event.target.textContent = "Show more";
            }
        }
    }
}
