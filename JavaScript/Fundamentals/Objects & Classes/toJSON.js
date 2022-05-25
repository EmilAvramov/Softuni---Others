function toJSON(firstName, lastName, hairColor) {
    var person = {
        name: firstName,
        lastName,
        hairColor,
    };
    console.log(JSON.stringify(person));
}

toJSON("George", "Jones", "Brown");
