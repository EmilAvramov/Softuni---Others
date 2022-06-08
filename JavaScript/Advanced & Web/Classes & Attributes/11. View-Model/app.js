class Textbox {
    constructor(selector, regex) {
        this._value = "";
        this._elements = document.querySelectorAll(selector);
        this._invalidSymbols = regex;
    }
    isValid() {
        this._invalidSymbols.test(this.value) ? false : true;
    }

    get value() {
        return this._value;
    }

    set value(input) {
        this._elements = this._elements.map(
            (element) => (element.value = input)
        );
        this._value = input;
    }

    get elements() {
        return this._elements;
    }
}

let textbox = new Textbox(".textbox", /[^a-zA-Z0-9]/);
let inputs = document.getElementsByClassName(".textbox");

inputs.addEventListener("click", function () {
    console.log(textbox.value);
});
