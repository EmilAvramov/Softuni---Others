function pascalCase(word) {
	return word.split(/(?=[A-Z])/).join(', ');
}

console.log(pascalCase('SplitMeIfYouCanHaHaYouCantOrYouCan'));
