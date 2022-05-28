function rectangle(width = 0, height = 0, color = "") {
    color = color[0].toUpperCase() + color.slice(1, color.length);
    var rectangle = {
        width,
        height,
        color,
        calcArea: function () {
            return this.width * this.height;
        },
    };
    return rectangle;
}


let rect = rectangle(4, 5, 'red');
console.log(rect.width);
console.log(rect.height);
console.log(rect.color);
console.log(rect.calcArea());