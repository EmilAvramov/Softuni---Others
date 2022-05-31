function generateReport() {
    let headers = Array.from(document.querySelectorAll(`thead tr th input`));
    let rows = document.querySelectorAll(`tbody tr`);

    let output = [];
    for (let i = 0; i < rows.length; i++) {
        let current = {};

        for (let j = 0; j < headers.length; j++) {
            if (headers[j].checked) {
                current[headers[j].name] = rows[i].children[j].textContent;
            }
        }

        output.push(current);
    }

    document.getElementById("output").value = JSON.stringify(output);
}
