class Company {
    constructor() {
        this.departments = {};
    }

    addEmployee(name, salary, position, department) {
        if (
            this.check(name) &&
            this.check(salary) &&
            this.check(position) &&
            this.check(department) &&
            salary >= 0
        ) {
            if (this.departments.hasOwnProperty(department)) {
                this.departments[department].push([name, salary, position]);
            } else {
                this.departments[department] = [[name, salary, position]];
            }
            return `New employee is hired. Name: ${name}. Position: ${position}`
        } else {
            throw "Invalid input!";
        }
    }

    bestDepartment() {
        let bestDeptName = "";
        let bestDeptEmployees = "";
        let highestAvg = Number.MIN_SAFE_INTEGER;
        let output = [];

        for (const property in this.departments) {
            let current = 0;
            let temp = 0;
            for (let employee of this.departments[property]) {
                temp += employee[1];
                current = temp / this.departments[property].length;
                if (current > highestAvg) {
                    highestAvg = current;
                    bestDeptEmployees = this.departments[property];
                    bestDeptName = property;
                }
            }
        }
        output.push(`Best Department is: ${bestDeptName}`);
        output.push(`Average salary: ${highestAvg.toFixed(2)}`);
        bestDeptEmployees = bestDeptEmployees
            .sort((a, b) => (a[0] > b[0] ? 1 : -1))
            .sort((a, b) => (a[1] > b[1] ? -1 : 1));
        for (let employee of bestDeptEmployees) {
            output.push(`${employee[0]} ${employee[1]} ${employee[2]}`);
        }
        return output.join("\n");
    }

    check(param) {
        if (param === "" || param === undefined || param === null) {
            return false;
        } else {
            return true;
        }
    }
}

let c = new Company();
c.addEmployee("Stanimir", 2000, "engineer", "Construction");
c.addEmployee("Pesho", 1500, "electrical engineer", "Construction");
c.addEmployee("Slavi", 500, "dyer", "Construction");
c.addEmployee("Stan", 2000, "architect", "Construction");
c.addEmployee("Stanimir", 1200, "digital marketing manager", "Marketing");
c.addEmployee("Pesho", 1000, "graphical designer", "Marketing");
c.addEmployee("Gosho", 1350, "HR", "Human resources");
console.log(c.bestDepartment());
