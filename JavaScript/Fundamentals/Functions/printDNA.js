function dna(repeats) {
    const letters = ["AT", "CG", "TT", "AG", "GG"];
    let current = "";
    for (let i = 0; i < repeats; i++) {
        current = letters[i % letters.length];
        if (i % 4 === 0) {
            console.log(`**${current[0]}${current[1]}**`);
        } else if (i % 4 === 1) {
            console.log(`*${current[0]}--${current[1]}*`);
        } else if (i % 4 === 2) {
            console.log(`${current[0]}----${current[1]}`);
        } else if (i % 4 === 3) {
            console.log(`*${current[0]}--${current[1]}*`);
        }
    }
}

dna(10);
dna(4);
