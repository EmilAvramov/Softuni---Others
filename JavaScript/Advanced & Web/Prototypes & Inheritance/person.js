class Person {
	constructor(first, last) {
		this._firstName = first;
		this._lastName = last;
		this._fullName = `${this.firstName} ${this.lastName}`;
	}

	get firstName() {
		return this._firstName;
	}

	set firstName(input) {
		this._firstName = input;
		this._fullName = `${input} ${this.lastName}`;
	}

	get lastName() {
		return this._lastName;
	}

	set lastName(input) {
		this._lastName = input;
		this._fullName = `${this.firstName} ${input}`;
	}

	get fullName() {
		return this._fullName;
	}

	set fullName(input) {
		this._fullName = input;
		this._firstName = input.split(' ')[0];
		this._lastName = input.split(' ')[1];
	}
}

let person = new Person('Peter', 'Ivanov');
console.log(person.fullName); //Peter Ivanov
person.firstName = 'George';
console.log(person.fullName); //George Ivanov
person.lastName = 'Peterson';
console.log(person.fullName); //George Peterson
person.fullName = 'Nikola Tesla';
console.log(person.firstName); //Nikola
console.log(person.lastName); //Tesla
