function addItem() {
    var parent = document.getElementById("items");
    var input = document.getElementById("newItemText");
    var button = document.querySelector("main input[type='button']");

    button.addEventListener("click", createItem(input, parent));
    parent.addEventListener("click", deleteItem)

    function createItem(input, parent) {
        let newLi = document.createElement("li");
        let delBtn = document.createElement("a");
        delBtn.href = "#";
        delBtn.textContent = "[Delete]";
        newLi.textContent = input.value;
        newLi.appendChild(delBtn);
        parent.appendChild(newLi);   
    }

    function deleteItem(element) {
        element.target.parentNode.remove()
    }
}
