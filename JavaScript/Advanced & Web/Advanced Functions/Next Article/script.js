function getArticleGenerator(articles) {
    let index = 0;
    return function () {
        if (articles[index]) {
            let create = document.createElement("div");
            create.textContent = articles[index];
            document.getElementById("content").appendChild(create);
            index++;
        }
    };
}
