function smallest(num1, num2, num3) {
	console.log([num1, num2, num3].sort((a, b) => a - b)[0]);
}

smallest(2, 5, 3);
smallest(600, 342, 123);
smallest(25, 21, 4);
