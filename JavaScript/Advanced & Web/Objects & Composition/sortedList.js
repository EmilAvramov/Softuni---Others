class createSortedList {
    constructor(list = []) {
        this.list = list.sort((a, b) => {
            a - b;
        });
        this.size = this.list.length;
    }

    add(element) {
        this.list.push(element);
    }

    remove(index) {
        this.list.splice(index, 1);
    }

    get(index) {
        return this.list[index];
    }
}

// function createSortedList() {
//     var list = {
//         main: [],
//         add: (element) => list.main.push(element),
//         remove: (index) => list.main.splice(index, 1),
//         get: (index) => {
//             return list.main[index];
//         },
//         size: () => {
//             return list.main.length;
//         },
//     };
//     return list.main;
// }

let list = new createSortedList();
list.add(5);
list.add(6);
list.add(7);
console.log(list.get(1));
list.remove(1);
console.log(list.get(1));