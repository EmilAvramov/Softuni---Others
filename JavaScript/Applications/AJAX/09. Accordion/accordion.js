async function getData() {
    let request = await fetch(
        "http://localhost:3030/jsonstore/advanced/articles/list"
    );
    return request.json();
}

async function getItem(id) {
    let request = await fetch(
        "http://localhost:3030/jsonstore/advanced/articles/details/" + id
    );
    return request.json();
}

function createElement(e) {
    return document.createElement(e);
}

function addEvent(e) {
    e.addEventListener("click", () => {
        let subParent = e.parentNode
        let child = subParent.parentNode.children[1]
        if (child.classList.contains("extra")) {
            child.classList.remove("extra")
            child.style.display = "inline-block"
            e.textContent = "Less"
        } else {
            child.classList.add("extra")
            child.style.display = ""
            e.textContent = "More"
        }
    })
}

function createCards(response) {
    response.then((parsed) => {
        console.log(Object.values(parsed));
        for (let property of Object.values(parsed)) {
            getItem(property._id).then((data) => {
                let mainDiv = createElement("div")
                mainDiv.classList.add("accordion")
                
                let subDiv = createElement("div")
                subDiv.classList.add("head")

                let span = createElement("span")
                span.textContent = data.title
                subDiv.appendChild(span)

                let btn = createElement("btn")
                btn.classList.add("button")
                btn.setAttribute("id", `${data._id}`);
                btn.textContent = "More"
                addEvent(btn)
                subDiv.appendChild(btn)

                let lastDiv = createElement("div")
                lastDiv.classList.add("extra")

                let p = createElement("p")
                p.textContent = data.content
                lastDiv.appendChild(p)

                mainDiv.appendChild(subDiv)
                mainDiv.appendChild(lastDiv)
                parent.appendChild(mainDiv)
            });
        }
    });
}

let parent = document.getElementById("main")

createCards(getData());
