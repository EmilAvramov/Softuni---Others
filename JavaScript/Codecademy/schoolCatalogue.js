//@ts-check

class School {
    /**
     * @param {string} name
     * @param {string} level
     * @param {number} students
     */
    constructor(name, level, students) {
        this._name = name;
        this._level = level;
        this._numberOfStudents = students;
    }

    get name() {
        return this._name;
    }
    get level() {
        return this._level;
    }
    get numberOfStudents() {
        return this._numberOfStudents;
    }
    set numberOfStudents(studentCount) {
        // @ts-ignore
        if (typeof studentCount === "Number") {
            this._numberOfStudents = studentCount;
        } else {
            console.log(
                "Invalid input: numberOfStudents must be set to a Number."
            );
        }
    }
    quickFacts() {
        console.log(
            `${this._name} educates ${this._numberOfStudents} students at the ${this._level} school level`
        );
    }
    /**
     * @param {Array} substituteTeachers
     */
    static pickSubstituteTeacher(substituteTeachers) {
        let index = Math.floor(Math.random() * (substituteTeachers.length - 1));
        return substituteTeachers[index];
    }
}

class PrimarySchool extends School {
    /**
     * @param {string} name
     * @param {number} students
     * @param {string} pickUp
     * @param {string} level
     */
    constructor(name, level, students, pickUp) {
        super(name, level = "primary", students);
        this._pickUpPolicy = pickUp;
    }
    get pickUpPolicy() {
        return this._pickUpPolicy;
    }
}

class Middle extends School {
    /**
     * @param {string} name
     * @param {string} level
     * @param {number} students
     */
    constructor(name, level, students) {
        super(name, (level = "middle"), students);
    }
}

class High extends School {
    /**
     * @param {string} name
     * @param {string} level
     * @param {number} students
     * @param {Array} sportsTeams
     */
    constructor(name, level, students, sportsTeams) {
        super(name, (level = "high"), students);
        this._sportsTeams = sportsTeams;
    }
    get sportsTeams() {
        return this._sportsTeams;
    }
}

const lorraineHansbury = new PrimarySchool(
    "Lorraine Hansbury",
    "primary",
    514,
    "Students must be picked up by a parent, guardian, or a family member over the age of 13."
);
console.log(lorraineHansbury);
