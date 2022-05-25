class Vehicle {
    constructor(type = "", model = "", parts = {}, fuel = 0) {
        this.type = type;
        this.model = model;
        this.parts = parts;
        this.fuel = fuel;
        this.parts.quality = parts.power * parts.engine;
    }
    drive(loss = 0) {
        this.fuel -= loss;
    }
}
/*
let parts = { engine: 6, power: 100 };
let vehicle = new Vehicle("a", "b", parts, 200);
vehicle.drive(100);
console.log(vehicle.fuel);
console.log(vehicle.parts.quality);
*/
let parts = { engine: 9, power: 500 };
let vehicle = new Vehicle("l", "k", parts, 840);
vehicle.drive(20);
console.log(vehicle.fuel);
