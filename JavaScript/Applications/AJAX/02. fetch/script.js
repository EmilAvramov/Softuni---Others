let button = document.getElementById("load");
let input = document.getElementById("username");
let result = document.getElementById("res");
const url = "https://api.github.com/users/";

button.addEventListener("click", () => {
    fetch(url + input.value + "/repos")
        .then((response) => response.json())
        .then((data) => {
            result.innerHTML = "";
            for (item of data) {
                let element = document.createElement("li");
                element.innerHTML = `<a href="http://${item.html_url}">${item.full_name}</a>`;
                result.append(element);
            }
        })
        .catch((error) => console.log(error));
});
