function calculator() {
    function calculate() {
        return {
            selector1: document.getElementById("num1").value,
            selector2: document.getElementById("num2").value,
            result: document.getElementById("result").value,
            add: () => selector1 + selector2,
            subtract: () => selector1 - selector2,
        };
    }
}
