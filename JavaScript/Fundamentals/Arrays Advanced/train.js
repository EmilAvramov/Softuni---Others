function train(arr) {
    let wagons, capacity, commands, passengers;
    [wagons, capacity, ...commands] = arr;
    wagons = wagons.split(" ").map(Number);
    capacity = Number(capacity);

    commands.forEach((command) => {
        if (command.includes("Add")) {
            wagons.push(command.split(" ")[1]);
        } else {
            passengers = Number(command);
            wagons.forEach((wagon) => {
                if (wagon < capacity && passengers > 0) {
                    if (passengers <= capacity - wagon) {
                        wagons[wagons.indexOf(wagon)] += passengers;
                        passengers = 0;
                    }
                }
            });
        }
    });
    console.log(wagons.join(" "));
}

train(["32 54 21 12 4 0 23", "75", "Add 10", "Add 0", "30", "10", "75"]);

train(["0 0 0 10 2 4", "10", "Add 10", "10", "10", "10", "8", "6"]);
