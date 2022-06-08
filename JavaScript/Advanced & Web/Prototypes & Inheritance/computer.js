function createComputerHierarchy() {
    class Computer {
        constructor(manuf, speed, ram, disk) {
            if (new.target == Computer) {
                throw new Error(
                    "Cannot make an instance of abstract class Computer"
                );
            }
            this.manufacturer = manuf;
            this.processorSpeed = speed;
            this.ram = ram;
            this.hardDiskSpace = disk;
        }
    }

    class Laptop extends Computer {
        constructor(manuf, speed, ram, disk, weight, color, battery) {
            super(manuf, speed, ram, disk);
            this.weight = weight;
            this.color = color;
            this._battery = battery;
        }

        get battery() {
            return this._battery;
        }

        set battery(obj) {
            if (!(obj instanceof Battery)) {
                throw new TypeError("Use the appropriate component");
            } else {
                this._battery = obj;
            }
        }
    }

    class Desktop extends Computer {
        constructor(manuf, speed, ram, disk, keyboard, monitor) {
            super(manuf, speed, ram, disk);
            this._keyboard = keyboard;
            this._monitor = monitor;
        }

        get keyboard() {
            return this._keyboard;
        }

        get monitor() {
            return this._monitor;
        }

        set keyboard(obj) {
            if (!(obj instanceof Keyboard)) {
                throw new TypeError("Use the appropriate component");
            } else {
                this._keyboard = obj;
            }
        }

        set monitor(obj) {
            if (!(obj instanceof Monitor)) {
                throw new TypeError("Use the appropriate component");
            } else {
                this._monitor = obj;
            }
        }
    }

    class Keyboard {
        constructor(manuf, time) {
            this.manufacturer = manuf;
            this.responseTime = time;
        }
    }

    class Monitor {
        constructor(manuf, width, height) {
            this.manufacturer = manuf;
            this.width = width;
            this.height = height;
        }
    }

    class Battery {
        constructor(manuf, expectedLife) {
            this.manufacturer = manuf;
            this.expectedLife = expectedLife;
        }
    }

    return {
        Computer,
        Laptop,
        Desktop,
        Monitor,
        Keyboard,
        Battery,
    };
}

let classes = createComputerHierarchy();
let Computer = classes.Computer;
let Laptop = classes.Laptop;
let Desktop = classes.Desktop;
let Monitor = classes.Monitor;
let Battery = classes.Battery;
let Keyboard = classes.Keyboard;

let battery = new Battery("Energy", 3);
console.log(battery);
let laptop = new Laptop(
    "Hewlett Packard",
    2.4,
    4,
    0.5,
    3.12,
    "Silver",
    battery
);
console.log(laptop);
