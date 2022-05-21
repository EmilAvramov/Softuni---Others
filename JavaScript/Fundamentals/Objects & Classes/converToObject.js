function convert(jsonStr) {
    let person = JSON.parse(jsonStr);
    for (const property in person) {
        console.log(`${property}: ${person[property]}`);
    }
}

convert('{"name": "George", "age": 40, "town": "Sofia"}');
