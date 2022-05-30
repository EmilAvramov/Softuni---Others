function validate() {
    var input = document.getElementById("email");
    const validate = /([a-z]+)@([a-z]+)\.([a-z]+)/;

    input.addEventListener("change", textChange);

    function textChange(event) {
        if (validate.test(event.target.value)) {
            event.target.classList.remove("error");
        } else {
            event.target.classList.add("error");
        }
    }
}
