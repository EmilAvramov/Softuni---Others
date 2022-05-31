function solve() {
    var data = document.getElementById("input").value.split(".");
    var result = document.getElementById("output");
    let count = 0;
    let p = document.createElement("p");
    data.forEach((element) => {
        if (element.length > 0) {
            element = element + ".";
            if (count === 3) {
                result.appendChild(p);
                count = 0;
                p = document.createElement("p");
            }
            p.innerHTML += element;
            count++;
        }
    });
    if (p.innerHTML !== "") {
        result.appendChild(p);
    }
}
