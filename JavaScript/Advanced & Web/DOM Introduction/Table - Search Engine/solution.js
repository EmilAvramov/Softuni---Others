function solve() {
    document.querySelector("#searchBtn").addEventListener("click", onClick);

    function onClick() {
        var search = document.getElementById("searchField").value;
        var contents = Array.from(
            document.querySelectorAll("body table tbody tr")
        );
        contents.forEach((content) => {
            content.classList.remove("select");
            if (content.innerHTML.includes(search)) {
                content.classList.add("select");
            }
        });
    }
}
