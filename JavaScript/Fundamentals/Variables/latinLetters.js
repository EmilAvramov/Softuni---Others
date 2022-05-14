function latins(string) {
  let word = "";
  for (let i = 0; i < Number(string); i++) {
    for (let j = 0; j < Number(string); j++) {
      for (let k = 0; k < Number(string); k++) {
        word += String.fromCharCode(97 + i);
        word += String.fromCharCode(97 + j);
        word += String.fromCharCode(97 + k);
        console.log(word);
        word = "";
      }
    }
  }
}

latins(2);
