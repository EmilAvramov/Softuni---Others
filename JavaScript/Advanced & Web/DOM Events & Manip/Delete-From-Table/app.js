function deleteByEmail() {
    var table = Array.from(document.querySelectorAll("#customers tbody"));
    var output = document.getElementById("result");
    var input = document.querySelector("label input[type='text']");
    var button = document.querySelector("body label button");

    button.addEventListener("click", deleteItem(table, input, output));

    function deleteItem(location, input, output) {
        let found = false;
        for (let data of location) {
            for (let i = 0; i < data.childElementCount; i++) {
                if (data.children[i].children[1].innerHTML === input.value) {
                    output.textContent = "Deleted";
                    found = true;
                    data.removeChild(data.children[i]);
                }
            }
        }
        if (!found) {
            output.textContent = "Not found.";
        }
    }
}
