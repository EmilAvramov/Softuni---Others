function create(words = []) {
    var parent = document.getElementById("content");
    for (let word of words) {
        parent.appendChild(create(word));
    }

    function create(string) {
        let div = document.createElement("div");
        let p = document.createElement("p");
        p.textContent = string;
        p.style.display = "none";
        div.addEventListener("click", show);
        div.appendChild(p);
        return div;
    }

    function show(event) {
        event.target.children[0].style.display = "block";
    }
}
