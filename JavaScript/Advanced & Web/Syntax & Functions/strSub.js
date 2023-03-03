function substring(word, text) {
	let textWords = text.split(' ');
	let found = false;

	for (let i = 0; i < textWords.length; i++) {
		if (textWords[i].toLowerCase() === word.toLowerCase()) {
			console.log(textWords[i].toLowerCase());
			found = true;
			break;
		}
	}

	if (found === false) {
		console.log(`${word} not found!`);
	}
}


substring('javascript',
'JavaScript is the best programming language')

substring('python',
'JavaScript is the best programming language')