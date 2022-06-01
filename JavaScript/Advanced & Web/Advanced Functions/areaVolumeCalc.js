//@ts-check

function area() {
    return Math.abs(this.x * this.y);
}
function vol() {
    return Math.abs(this.x * this.y * this.z);
}

/**
 * @param {{ (): number; (): number; }} func1
 * @param {{ (): number; (): number; }} func2
 * @param {string} string
 */
function areaVolume(func1, func2, string) {
    let arr = JSON.parse(string);
    const result = arr.map((/** @type {any} */ el) => ({
        area: func1.call(el),
        volume: func2.call(el),
    }));
    return result;
}

areaVolume(
    area,
    vol,
    `[
    {"x":"1","y":"2","z":"10"},
    {"x":"7","y":"7","z":"10"},
    {"x":"5","y":"2","z":"10"}
    ]`
);

areaVolume(
    area,
    vol,
    `[
    {"x":"10","y":"-22","z":"10"},
    {"x":"47","y":"7","z":"-5"},
    {"x":"55","y":"8","z":"0"},
    {"x":"100","y":"100","z":"100"},
    {"x":"55","y":"80","z":"250"}
    ]`
);
