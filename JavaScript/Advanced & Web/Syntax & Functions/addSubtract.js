function addSubtract(num1, num2, num3) {
	function sum() {
		return num1 + num2;
	}

	function subtract() {
		return sum() - num3;
	}

	return subtract();
}

console.log(addSubtract(23, 6, 10));
console.log(addSubtract(1, 17, 30));
