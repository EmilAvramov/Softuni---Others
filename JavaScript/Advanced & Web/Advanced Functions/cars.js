function cars(arr) {
    var commands = function () {
        var privateRepo = [];
        return {
            create: (name) => {}, // push named object
            inherits: (name, parent) => {}, // clone named object from parent
            set: (name, key, value) => {}, // set property of named object
            print: (name) => {}, // filter objects by their name
        };
    };

    for (let car of arr) {
        let command, others;
        [command, ...others] = car.split(" ");
        // move through commands and call closure
    }
}

cars([
    "create c1",
    "create c2 inherit c1",
    "set c1 color red",
    "set c2 model new",
    "print c1",
    "print c2",
]);
