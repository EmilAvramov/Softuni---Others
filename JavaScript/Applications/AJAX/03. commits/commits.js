let button = document.getElementById("load");
let username = document.getElementById("username");
let repo = document.getElementById("repo");
let result = document.getElementById("res");
const url = "https://api.github.com/repos/";

button.addEventListener("click", () => {
    fetch(url + username.value + "/" + repo.value + "/commits")
        .then((response) => response.json())
        .then((data) => {
            result.innerHTML = "";
            for (item of data) {
                let element = document.createElement("li");
                element.textContent = `${item.commit.author.name}: ${item.commit.message}`;
                result.append(element);
            }
        })
        .catch((error) => {
            let element = document.createElement("li");
            element.textContent = `"Error: ${error.status} (Not Found)`;
            result.append(element);
        });
});
