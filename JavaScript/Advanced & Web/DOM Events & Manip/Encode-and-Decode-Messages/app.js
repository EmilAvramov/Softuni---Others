function encodeAndDecodeMessages() {
    var encodeBox = document.getElementsByTagName("textarea")[0];
    var encodeBtn = document.getElementsByTagName("button")[0];
    var decodeBox = document.getElementsByTagName("textarea")[1];
    var decodeBtn = document.getElementsByTagName("button")[1];

    encodeBtn.addEventListener("click", encode(encodeBox, decodeBox));
    decodeBtn.addEventListener("click", decode(decodeBox))

    function encode(source, target) {
        let message = source.value;
        let newMsg = "";
        for (let i = 0; i < message.length; i++) {
            newMsg += String.fromCodePoint(message[i].charCodeAt(0) + 1);
        }
        target.value = newMsg;
        source.value = "";
    }

    function decode(source) {
        let message = source.value;
        let newMsg = "";
        for (let i = 0; i < message.length; i++) {
            newMsg += String.fromCodePoint(message[i].charCodeAt(0) - 1);
        }
        source.value = newMsg;
    }
}
