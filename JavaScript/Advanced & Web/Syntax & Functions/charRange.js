function charRange(char1, char2) {
	const code1 = char1.charCodeAt(0);
	const code2 = char2.charCodeAt(0);
	const symArray = [];

	if (code1 >= code2) {
		for (let i = code2 + 1; i < code1; i++) {
			symArray.push(String.fromCharCode(i));
		}
	} else {
		for (let i = code1 + 1; i < code2; i++) {
			symArray.push(String.fromCharCode(i));
		}
	}

	console.log(symArray.join(' '));
}

charRange('C', '#');
charRange('#', ':');
