function solution() {
    let masterStr = "";

    return {
        append: (str) => {
            masterStr += str;
        },
        removeStart: (n) => {
            masterStr = masterStr.slice(n, masterStr.length);
        },
        removeEnd: (n) => {
            masterStr = masterStr.slice(0, masterStr.length - n);
        },
        print: () => console.log(masterStr),
    };
}

let firstZeroTest = solution();

firstZeroTest.append("hello");
firstZeroTest.append("again");
firstZeroTest.removeStart(3);
firstZeroTest.removeEnd(4);
firstZeroTest.print();


let secondZeroTest = solution();

secondZeroTest.append('123');
secondZeroTest.append('45');
secondZeroTest.removeStart(2);
secondZeroTest.removeEnd(1);
secondZeroTest.print();