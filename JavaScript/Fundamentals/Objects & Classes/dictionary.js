function dict(jsonStr = []) {
    let dictionary = {};
    jsonStr.forEach((element) => {
        let parsed = JSON.parse(element);
        for (const property in parsed) {
            dictionary[property] = parsed[property];
        }
    });
    dictionary = Object.keys(dictionary)
        .sort()
        .reduce((obj, key) => {
            obj[key] = dictionary[key];
            return obj;
        }, {});
    for (const property in dictionary) {
        console.log(`Term: ${property} => Definition: ${dictionary[property]}`);
    }
}

dict([
    '{"Coffee":"A hot drink made from the roasted and ground seeds (coffee beans) of a tropical shrub."}',
    '{"Bus":"A large motor vehicle carrying passengers by road, typically one serving the public on a fixed route and for a fare."}',
    '{"Boiler":"A fuel-burning apparatus or container for heating water."}',
    '{"Tape":"A narrow strip of material, typically used to hold or fasten something."}',
    '{"Microphone":"An instrument for converting sound waves into electrical energy variations which may then be amplified, transmitted, or recorded."}',
]);
