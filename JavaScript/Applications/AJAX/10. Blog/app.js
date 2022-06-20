async function getPosts() {
    let response = await fetch("http://localhost:3030/jsonstore/blog/posts");
    return response.json();
}

async function getComments() {
    let response = await fetch("http://localhost:3030/jsonstore/blog/comments");
    return response.json();
}

let btnLoad = document.getElementById("btnLoadPosts");
let btnView = document.getElementById("btnViewPost");
let select = document.getElementById("posts");
let listOutput = document.getElementById("post-comments");
let titleOutput = document.getElementById("post-title");
let bodyOutput = document.getElementById("post-body");

btnLoad.addEventListener("click", () => {
    getPosts().then((data) => {
        for (let [key, value] of Object.entries(data)) {
            let el = document.createElement("option");
            el.value = key;
            el.innerHTML = value.title;
            select.appendChild(el);
        }
    });
});

btnView.addEventListener("click", () => {
    getPosts().then((data) => {
        for (let property of Object.values(data)) {
            if (select.value === property.id) {
                titleOutput.textContent = property.title;
                bodyOutput.textContent = property.body;
            }
        }
    });

    getComments().then((data) => {
        listOutput.innerHTML = "";
        for (let property of Object.values(data)) {
            let el = document.createElement("li");
            if (select.value === property.postId) {
                el.textContent = property.text;
                listOutput.appendChild(el);
            }
        }
    });
});
