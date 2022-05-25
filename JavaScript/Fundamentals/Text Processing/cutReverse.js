function cutReverse(string = "") {
    let subA = string.substring(0, string.length / 2);
    let subB = string.substring(string.length / 2, string.length);
    subA = subA.split("").reverse().join("");
    subB = subB.split("").reverse().join("");

    console.log(subA);
    console.log(subB);
}

cutReverse("tluciffiDsIsihTgnizamAoSsIsihT");
cutReverse("sihToDtnaCuoYteBIboJsihTtAdooGoSmI");
