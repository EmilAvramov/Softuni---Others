function ladyBugs(arr) {
  let fieldSize, bugPos, commands;
  let field = [];
  [fieldSize, bugPos, ...commands] = arr;
  fieldSize = Number(fieldSize);
  bugPos = bugPos.split(" ").map(Number);
  for (let i = 0; i < fieldSize; i++) {
    field.push(0);
  }
  for (let i = 0; i < bugPos.length; i++) {
    if (bugPos[i] < field.length) {
      field[bugPos[i]] = 1;
    }
  }

  commands.forEach((element) => {
    element = element.split(" ");
    let pos = Number(element[0]);
    let command = element[1];
    let distance = Number(element[2]);
    if (pos < fieldSize && pos >= 0 && field[pos] === 1) {
      if (command === "right") {
        if (pos + distance >= fieldSize) {
          field[pos] = 0;
        } else if (field[pos + distance] === 0) {
          field[pos] = 0;
          field[pos + distance] = 1;
        } else {
          for (let i = pos + distance + 1; i > 0; i++) {
            if (field[i] === 0) {
              field[pos] = 0;
              field[pos + distance] = 1;
              break;
            } else if (i >= fieldSize) {
              field[pos] = 0;
              break;
            }
          }
        }
      } else {
        if (pos - distance < 0) {
          field[pos] = 0;
        } else if (field[pos - distance] === 0) {
          field[pos] = 0;
          field[pos - distance] = 1;
        } else {
          for (let i = pos - distance + 1; i >= 0; i--) {
            if (field[i] === 0) {
              field[pos] = 0;
              field[pos - distance] = 1;
              break;
            } else if (i <= fieldSize) {
              field[pos] = 0;
              break;
            }
          }
        }
      }
    }
  });
  console.log(field.join(" "));
}

ladyBugs([3, "0 1", "0 right 1", "2 right 1"]);
ladyBugs([3, "0 1 2", "0 right 1", "1 right 1", "2 right 1"]);
ladyBugs([5, "3", "3 left 2", "1 left -2"]);
