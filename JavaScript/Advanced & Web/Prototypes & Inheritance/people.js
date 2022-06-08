function solution() {
    class Employee {
        constructor(name, age, salary = 0, tasks = []) {
            this.name = name;
            this.age = age;
            this.salary = salary;
            this.tasks = tasks;
            this.index = -1;
        }

        work() {
            this.index++;
            if (this.index >= this.tasks.length) {
                this.index = 0;
            }
            return console.log(this.tasks[this.index]);
        }

        collectSalary() {
            return console.log(
                `${this.name} received ${this.salary} this month.`
            );
        }
    }
    class Junior extends Employee {
        constructor(name, age) {
            super(name, age);
            this.tasks = [`${this.name} is working on a simple task.`];
            this.index = -1;
        }
    }
    class Senior extends Employee {
        constructor(name, age) {
            super(name, age);
            this.tasks = [
                `${this.name} is working on a complicated task.`,
                `${this.name} is taking time off work.`,
                `${this.name} is supervising junior workers.`,
            ];
            this.index = -1;
        }
    }
    class Manager extends Employee {
        constructor(name, age) {
            super(name, age);
            this.tasks = [
                `${this.name} scheduled a meeting.`,
                `${this.name} is preparing a quarterly report.`,
            ];
            this.dividend = 0;
            this.index = -1;
        }
        collectSalary() {
            return console.log(
                `${this.name} received ${
                    this.salary + this.dividend
                } this month.`
            );
        }
    }
    return {
        Employee,
        Junior,
        Senior,
        Manager,
    };
}

const classes = solution();
const junior = new classes.Junior("Ivan", 25);
junior.work();
junior.work();
junior.salary = 5811;
junior.collectSalary();
const sinior = new classes.Senior("Alex", 31);
sinior.work();
sinior.work();
sinior.work();
sinior.work();
sinior.salary = 12050;
sinior.collectSalary();
const manager = new classes.Manager("Tom", 55);
manager.salary = 15000;
manager.collectSalary();
manager.dividend = 2500;
manager.collectSalary();
