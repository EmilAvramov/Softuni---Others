function palindromes(arr) {
	arr.forEach((num) => {
		let string = num.toString();
		if (string === string.split('').reverse().join('')) {
			console.log(true);
		} else {
			console.log(false);
		}
	});
}

palindromes([123, 323, 421, 121]);
