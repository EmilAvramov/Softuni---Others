function employees(arr = []) {
    let empObject = {};
    arr.forEach((employee) => {
        empObject[employee] = employee.length;
        console.log(
            `Name: ${employee} -- Personal Number: ${empObject[employee]}`
        );
    });
}

employees([
    "Silas Butler",
    "Adnaan Buckley",
    "Juan Peterson",
    "Brendan Villarreal",
]);
