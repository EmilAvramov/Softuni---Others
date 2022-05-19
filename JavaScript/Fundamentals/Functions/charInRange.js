function charRange(char1, char2) {
  let first, second;
  let between = [];
  if (char1.codePointAt() > char2.codePointAt()) {
    first = char2;
    second = char1;
  } else {
    first = char1;
    second = char2;
  }
  for (let i = first.codePointAt() + 1; i < second.codePointAt(); i++) {
    between.push(String.fromCharCode(i));
  }
  console.log(between.join(" "));
}

charRange("#", ":");
charRange("C", "#");
