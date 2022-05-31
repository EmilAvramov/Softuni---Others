function solve() {
    var check = document.querySelectorAll("button")[0];
    var clear = document.querySelectorAll("button")[1];
    var fields = document.querySelectorAll("tbody tr td input");
    var result = document.querySelector("#check p");
    var sudokuTable = document.querySelector("table");

    check.addEventListener("click", test);
    clear.addEventListener("click", clearBoard);

    function test() {
        // Rows
        let row1 = fields[0].value + fields[1].value + fields[2].value;
        let row2 = fields[3].value + fields[4].value + fields[5].value;
        let row3 = fields[6].value + fields[7].value + fields[8].value;
        // Columns
        let col1 = fields[0].value + fields[3].value + fields[6].value;
        let col2 = fields[1].value + fields[4].value + fields[7].value;
        let col3 = fields[2].value + fields[5].value + fields[8].value;
        // Table
        let table = [row1, row2, row3, col1, col2, col3].map(Number);
        if (table.forEach(element => {return element === table[0]})) {
            result.textContent = "You solve it! Congratulations!";
            result.style.color = "green";
            sudokuTable.style.border = "2px solid green";
        } else {
            result.textContent = "NOP! You are not done yet...";
            result.style.color = "red";
            sudokuTable.style.border = "2px solid red";
        }
    }

    function clearBoard() {
        for (let field of fields) {
            field.value = "";
            result.textContent = "";
            sudokuTable.style.border = "none";
        }
    }
}
