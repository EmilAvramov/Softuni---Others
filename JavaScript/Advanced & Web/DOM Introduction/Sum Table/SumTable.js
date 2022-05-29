function sumTable() {
    var rows = document.querySelectorAll("tbody tr td");
    let sum = 0;
    let index = 0;
    for (let row of rows) {
        index++;
        if (index % 2 === 0) {
            sum += Number(row.innerHTML);
        }
    }
    document.getElementById("sum").innerText = sum;
}
