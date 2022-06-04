function calculator() {
    var calculateObj = {
        first: 0,
        second: 0,
        result: 0,
        init: (selector1, selector2, resultSelector) => {
            calculateObj.first = selector1.value;
            calculateObj.second = selector2.value;
            calculateObj.result = resultSelector.value;
        },
        add: () => {
            this.result = this.first + this.second;
            return this.result;
        },
        subtract: () => {
            this.result = this.second - this.first;
            return this.result;
        },
    };
    return calculateObj;
}

const calculate = calculator();
calculate.init("#num1", "#num2", "#result");
