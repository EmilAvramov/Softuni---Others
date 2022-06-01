function closures(arr) {
    let command = (function () {
        let output = [];
        return {
            add: (str) => output.push(str),
            remove: (str) => {
                while (output.includes(str)) {
                    output.splice(output.indexOf(str), 1);
                }
            },
            print: () => console.log(output.join(",")),
        };
    })();

    arr.forEach((element) => {
        let cmd, arg;
        cmd = element.split(" ")[0];
        if (element !== "print") {
            arg = element.split(" ")[1];
        } else {
            arg = "";
        }
        command[cmd](arg);
    });
}

closures([
    "add hello",
    "add again",
    "remove hello",
    "add again",
    "remove hello",
    "print",
]);
closures(["add pesho", "add george", "add peter", "remove peter", "print"]);
