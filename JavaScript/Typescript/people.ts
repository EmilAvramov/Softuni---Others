class Employee {
	constructor(
		public name: string,
		public age: number,
		public salary: number = 0,
		public tasks: Array<string> = []
	) {}

	work(): void {
		console.log(this.tasks[0]);
		let temp: string = '';
		this.tasks = this.tasks.splice(0, 1);
		this.tasks.push(temp);
	}

	collectSalary(): void {
		console.log(`${this.name} received ${this.getSalary()}`);
	}

	getSalary(): number {
		return this.salary;
	}
}

class Junior extends Employee {
	constructor(name: string, age: number) {
		super(name, age);
		this.tasks = [`${name} is working on a simple task.`];
	}
}

class Senior extends Employee {
	constructor(name: string, age: number) {
		super(name, age);
		this.tasks = [
			`${name} is working on a complicated task.`,
			`${name} is taking time off work.`,
			`${name} is supervising junior workers.`,
		];
	}
}

class Manager extends Employee {
	constructor(name: string, age: number, public dividend: number = 0) {
		super(name, age);
		this.tasks = [
			`${name} scheduled a meeting.`,
			`${name} is preparing a quarterly report.`,
		];
	}

	public getSalary(): number {
		return this.getSalary() + this.dividend;
	}
}
