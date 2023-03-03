function revealWords(words, phrase) {
	let replacements = words.split(', ').map((word) => word.trim());
    let splitPhrase = phrase.split(' ')

    replacements.forEach((replacement, _) => {
        let replaceLength = replacement.length
        splitPhrase.forEach((word, index) => {
            let wordLength = word.length
            if (word.indexOf('*') >= 0 && wordLength === replaceLength) {
                splitPhrase[index] = replacement
            }
        })
    })

    return splitPhrase.join(' ')
}

console.log(
	revealWords(
		'great',
		'softuni is ***** place for learning new programming languages'
	)
);

console.log(
	revealWords(
		'great, learning',
		'softuni is ***** place for ******** new programming languages'
	)
);
