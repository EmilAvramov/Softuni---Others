function attachGradientEvents() {
    var target = document.getElementById("gradient");
    var result = document.getElementById("result");

    target.addEventListener("mousemove", logMouse);
    target.addEventListener("mouseout", mouseOut);

    function logMouse(event) {
        let percentage = event.offsetX / (event.target.clientWidth - 1);
        percentage = Math.trunc(percentage * 100);
        result.textContent = `${percentage}%`;
    }

    function mouseOut() {
        result.textContent = "";
    }
}
