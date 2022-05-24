function occurences(data) {
    var map = new Map();
    var result = [];
    data = data.split(" ");
    for (let line of data) {
        line = line.toLowerCase();
        if (!map.has(line)) {
            map.set(line, 1);
        } else {
            map.set(line, map.get(line) + 1);
        }
    }
    for (const [key, value] of map) {
        if (value % 2 !== 0) {
            result.push(key);
        }
    }
    console.log(result.join(" "));
}

occurences("Java C# Php PHP Java PhP 3 C# 3 1 5 C#");
occurences("Cake IS SWEET is Soft CAKE sweet Food");
