function cats(arr = []) {
    let cats = [];
    let currentCat = "";
    class Cat {
        constructor(name, age) {
            this.name = name;
            this.age = age;
        }
        meow() {
            return `${this.name}, age ${this.age} says Meow`;
        }
    }
    for (let i = 0; i < arr.length; i++) {
        currentCat = arr[i].split(" ");
        cats.push(new Cat(currentCat[0], currentCat[1]));
    }
    cats.forEach((cat) => {
        console.log(cat.meow());
    });
}

cats(["Mellow 2", "Tom 5"]);
cats(["Candy 1", "Poppy 3", "Nyx 2"]);
