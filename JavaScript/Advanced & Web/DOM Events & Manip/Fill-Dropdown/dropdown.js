function addItem() {
    var output = document.getElementById("menu");
    var textInput = document.getElementById("newItemText");
    var valueInput = document.getElementById("newItemValue");
    var button = document.querySelectorAll("input[type='button']")[0];

    button.addEventListener("click", create(textInput, valueInput));

    function create(text, val) {
        let element = document.createElement("option");
        element.textContent = text.value;
        element.value = val.value;
        output.appendChild(element);
        text.value = "";
        val.value = "";
    }
}
