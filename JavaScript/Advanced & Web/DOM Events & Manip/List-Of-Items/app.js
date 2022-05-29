function addItem() {
    var input = document.getElementById("newItemText");
    var target = document.querySelector("input[type='button']");
    var list = document.getElementById("items")
    target.addEventListener("click", createNew(input, list));

    function createNew(input, parent) {
        var next = document.createElement("li");
        next.textContent = input.value;
        parent.appendChild(next);
    }
}
