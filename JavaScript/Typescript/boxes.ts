class Box<T> {
	public elements: Array<number> = [];
	public type: T;

	constructor() {}

	add(element: number): void {
		this.elements.push(element);
	}

	remove(): void {
		this.elements.pop();
	}

	count(): number {
		return this.elements.length;
	}
}

let box = new Box<Number>();

box.add(1);

box.add(2);

box.add(3);

console.log(box.count);
