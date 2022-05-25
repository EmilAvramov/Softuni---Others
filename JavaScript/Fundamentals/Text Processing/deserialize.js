function deserialize(arr = []) {
    var command = arr.pop();
    let output = [];
    let data = {};
    for (let line of arr) {
        let letter = line.split(":")[0];
        let indices = line.split(":")[1].split("/");
        data[letter] = indices;
        for (let i = 0; i < indices.length; i++) {
            output.push("*");
        }
    }
    for (const property in data) {
        for (let value of data[property]) {
            output.splice(Number(value), 1, property);
        }
    }
    console.log(output.join(""));
}

deserialize(["a:0/2/4/6", "b:1/3/5", "end"]);
deserialize([
    "a:0/3/5/11",
    "v:1/4",
    "j:2",
    "m:6/9/15",
    "s:7/13",
    "d:8/14",
    "c:10",
    "l:12",
    "end",
]);
