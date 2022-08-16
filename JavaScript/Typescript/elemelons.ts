class Melon {
	public elementIndex: number;

	constructor(public weight: number, public melonSort: string) {
		this.elementIndex = this.weight = this.melonSort.length;
	}

	getElementIndex(): number {
		return this.elementIndex;
	}

	toString(): string {
		return `Element: ${this.melonSort}\nSort: ${this.melonSort}\nElement Index: ${this.elementIndex}`;
	}
}

class Watermelon extends Melon {
	constructor(weight: number, melonSort: string) {
		super(weight, melonSort);
	}
}

class Firemelon extends Melon {
	constructor(weight: number, melonSort: string) {
		super(weight, melonSort);
	}
}

class Earthmelon extends Melon {
	constructor(weight: number, melonSort: string) {
		super(weight, melonSort);
	}
}

class Airmelon extends Melon {
	constructor(weight: number, melonSort: string) {
		super(weight, melonSort);
	}
}

class Melolemonmelon extends Watermelon {
	public elements: Array<any> = [Firemelon, Earthmelon, Airmelon, Watermelon];

	constructor(weight: number, melonSort: string) {
		super(weight, melonSort);
	}
	morph() {
		let currentClass = this.elements.shift();
		this.elements.push(currentClass);
		return currentClass;
	}
}

let test: Melon = new Melon(100, 'Test');
let watermelon: Watermelon = new Watermelon(12.5, 'Kingsize');

console.log(watermelon.toString());
