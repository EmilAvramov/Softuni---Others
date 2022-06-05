class List {
    constructor() {
        this.data = []
        this.size = 0
    }

    add(el) {
        this.data.push(el);
        this.size++
    }

    remove(index) {
        if (index >= 0 && index < this.size) {
            this.data.splice(index, 1);
            this.size--
        }
    }

    get(index) {
        this.data = this.data.sort((a, b) => (a > b ? 1 : -1));
        if (index >= 0 && index < this.size) {
            return this.data[index]
        }
    }
}

let list = new List();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(0));
list.remove(1);
console.log(list.get(1));
