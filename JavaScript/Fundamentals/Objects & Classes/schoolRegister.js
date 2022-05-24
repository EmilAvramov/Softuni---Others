function schoolRegister(data) {
    function average(arr) {
        return arr.reduce((a, b) => a + b, 0) / arr.length;
    }

    let schoolRegister = {};

    for (let line of data) {
        let tokens = line.split(", ");
        let grade = Number(tokens[1].split(": ")[1]) + 1;
        let name = tokens[0].split(": ")[1];
        let score = Number(tokens[2].split(": ")[1]);
        if (score > 3) {
            let student = { name, score };
            if (!schoolRegister.hasOwnProperty(grade)) {
                schoolRegister[grade] = [];
            }
            schoolRegister[grade].push(student);
        }
    }
    let sortedGrades = Object.keys(schoolRegister).sort((a, b) => a - b);
    for (let grade of sortedGrades) {
        let students = schoolRegister[grade];
        console.log(`${grade} Grade`);
        console.log(
            `List of students: ${students.map((s) => s.name).join(", ")}`
        );
        console.log(
            `Average annual score from last year: ${average(
                students.map((s) => s.score)
            ).toFixed(2)}`
        );
        console.log();
    }
}
/*
    function printGrades(currentGrade, students, sum) {
        console.log(`${Number(currentGrade) + 1} Grade`);
        console.log(`List of students: ${students.join(", ")}`);
        console.log(
            `Average annual score from last year: ${(
                sum / students.length
            ).toFixed(2)}`
        );
        console.log();
    }

    var validData = [];
    let currentGrade = 0,
        sum = 0,
        students = [];

    data.forEach((element) => {
        if (element.split(", ")[2].split(": ")[1] > 3) {
            validData.push(element);
        }
    });

    validData = validData.sort((a, b) => {
        return (
            a.split(", ")[1].split(": ")[1] - b.split(", ")[1].split(": ")[1]
        );
    });

    validData.forEach((element) => {
        let grade = element.split(", ")[1].split(": ")[1];
        let student = element.split(", ")[0].split(": ")[1];
        let score = Number(element.split(", ")[2].split(": ")[1]);
        if (currentGrade === grade) {
            sum += score;
            students.push(student);
        } else {
            currentGrade = grade;
            sum = 0;
            students = [];
            sum += score;
            students.push(student);
        }
        if (validData.indexOf(element) !== validData.length - 1) {
            printGrades(currentGrade, students, sum);
        }
    });
    */

schoolRegister([
    "Student name: Mark, Grade: 8, Graduated with an average score: 4.75",
    "Student name: Ethan, Grade: 9, Graduated with an average score: 5.66",
    "Student name: George, Grade: 8, Graduated with an average score: 2.83",
    "Student name: Steven, Grade: 10, Graduated with an average score: 4.20",
    "Student name: Joey, Grade: 9, Graduated with an average score: 4.90",
    "Student name: Angus, Grade: 11, Graduated with an average score: 2.90",
    "Student name: Bob, Grade: 11, Graduated with an average score: 5.15",
    "Student name: Daryl, Grade: 8, Graduated with an average score: 5.95",
    "Student name: Bill, Grade: 9, Graduated with an average score: 6.00",
    "Student name: Philip, Grade: 10, Graduated with an average score: 5.05",
    "Student name: Peter, Grade: 11, Graduated with an average score: 4.88",
    "Student name: Gavin, Grade: 10, Graduated with an average score: 4.00",
]);

// schoolRegister([
//     "Student name: George, Grade: 5, Graduated with an average score: 2.75",
//     "Student name: Alex, Grade: 9, Graduated with an average score: 3.66",
//     "Student name: Peter, Grade: 8, Graduated with an average score: 2.83",
//     "Student name: Boby, Grade: 5, Graduated with an average score: 4.20",
//     "Student name: John, Grade: 9, Graduated with an average score: 2.90",
//     "Student name: Steven, Grade: 2, Graduated with an average score: 4.90",
//     "Student name: Darsy, Grade: 1, Graduated with an average score: 5.15",
// ]);
