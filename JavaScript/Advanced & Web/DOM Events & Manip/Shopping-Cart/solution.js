function solve() {
    var button = Array.from(document.getElementsByClassName("add-product"));
    var textArea = document.getElementsByTagName("textarea")[0];
    var checkout = document.getElementsByClassName("checkout")[0];
    let products = new Set();
    let total = 0;

    button.forEach((btn) => btn.addEventListener("click", added));
    checkout.addEventListener("click", finished);

    function added(event) {
        var parent = event.target.parentNode;
        var eventProduct = parent.parentNode.children[1].children[0].textContent;
        var eventPrice = parent.parentNode.children[3].textContent;
        products.add(eventProduct);
        total += Number(eventPrice);
        textArea.value += `Added ${eventProduct} for ${eventPrice} to the cart.\n`;
    }

    function finished() {
        let result = [...products];
        textArea.value += `You bought ${result.join(", ")} for ${total.toFixed(2)}.`;
        disableButtons()
    }

    function disableButtons() {
        var buttons = Array.from(document.getElementsByTagName("button"));
        buttons.forEach((button) => (button.disabled = true));
    }
}
