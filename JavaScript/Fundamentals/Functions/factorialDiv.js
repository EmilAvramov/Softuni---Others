function factorials(num1, num2) {
    function calcFact(num) {
        let sumF = 1;
        for (let i = num; i > 1; i--) {
            sumF *= i;
        }
        return sumF;
    }
    console.log((calcFact(num1) / calcFact(num2)).toFixed(2));
}

factorials(5, 2);
factorials(6, 2);
