function add(a) {
    var add = a;

    function f(b) {
        add += b;
        return f;
    }
    f.toString = function () {return add};
    return f;
}

console.log(add(1).toString());
console.log(add(6).toString());
console.log(add(-3).toString());
