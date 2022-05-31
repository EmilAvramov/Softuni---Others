function solve() {
    var resultBox = document.querySelector("#results");
    var resultTxt = document.querySelector("#results li h1");
    var sections = document.querySelectorAll("section");
    var answers = document.querySelectorAll(".answer-text");

    let answerCount = 0;
    let currentSection = 1;

    for (let answer of answers) {
        answer.addEventListener("click", nextPage);
    }

    function nextPage(event) {
        const rightAnswers = [
            "onclick",
            "JSON.stringify()",
            "A programming API for HTML and XML documents",
        ];
        if (rightAnswers.includes(event.target.textContent)) {
            answerCount += 1;
        }
        if (currentSection === 1) {
            sections[0].style.display = "none"
            sections[1].style.display = "block"
        } else if (currentSection === 2) {
            sections[1].style.display = "none"
            sections[2].style.display = "block"
        } else if (currentSection === 3) {
            sections[2].style.display = "none"
            outcome();
        }
        currentSection++;
    }

    function outcome() {
        resultBox.style.display = "block";
        if (answerCount === 3) {
            resultTxt.textContent = "You are recognized as top JavaScript fan!";
        } else {
            resultTxt.textContent = `You have ${answerCount} right answers`;
        }
    }
}
