function JSONtoHTML(arr = []) {
    arr = JSON.parse(arr);

    console.log("<table>");
    console.log(compileHeader(arr));
    arr.forEach((object) => {
        console.log(compileData(object));
    });
    console.log("</table>");

    function compileHeader(arr) {
        let headerContent = "";
        Object.keys(arr[0]).forEach((element) => {
            headerContent += "<th>" + validate(element) + "</th>";
        });
        return "   " + "<tr>" + headerContent + "</tr>";
    }

    function compileData(object) {
        let dataContent = "";
        Object.values(object).forEach((element) => {
            dataContent += "<td>" + validate(element) + "</td>";
        });
        return "   " + "<tr>" + dataContent + "</tr>";
    }

    function validate(data) {
        return data
            .toString()
            .replace(/&/g, "&amp;")
            .replace(/</g, "&lt;")
            .replace(/>/g, "&gt;")
            .replace(/"/g, "&quot;")
            .replace(/'/g, "&#39;");
    }
}

JSONtoHTML(`[{"Name":"Stamat",
"Score":5.5},
{"Name":"Rumen",
"Score":6}]`);

JSONtoHTML(`[{"Name":"Pesho>",
"Score":4,
"Grade":8},
{"Name":"Gosho",
"Score":5,
"Grade":8},
{"Name":"Angel",
"Score":5.50,
"Grade":10}]`);
