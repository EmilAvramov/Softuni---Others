class Circle {
    constructor(radius) {
        this.radius = radius
        this._diameter = 2 * radius
        this._area = Math.PI * (this.radius ** 2)
    }
    
    set diameter(input) {
        this.radius = input / 2
        this._diameter = this.radius * 2
    }

    get diameter() {
        return this._diameter
    }

    get area() {
        return Math.PI * (this.radius ** 2)
    }
}

let c = new Circle(2);
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);
c.diameter = 1.6;
console.log(`Radius: ${c.radius}`);
console.log(`Diameter: ${c.diameter}`);
console.log(`Area: ${c.area}`);