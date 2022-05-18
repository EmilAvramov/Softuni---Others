function ladyBugs(arr) {
  let fieldSize, bugPos, commands;
  [fieldSize, bugPos, ...commands] = arr;
  fieldSize = Number(fieldSize);
  bugPos = bugPos.split(" ").map(Number);

  commands.forEach((element, index) => {
    element = element.split(" ");
    let pos = Number(element[0]);
    let command = element[1];
    let distance = Number(element[2]);
    if (bugPos.indexOf(pos)) {
      if (command === "right") {
        if (index + distance > fieldSize - 1) {
          bugPos[index] = 0;
        } else if (element[index + distance] === 0) {
          bugPos[index] = 0;
          bugPos[index + distance] = 1;
        } else {
          for (let i = index + distance + 1; i > 0; i++) {
            if (bugPos[i] === 0) {
              bugPos[index] = 0;
              bugPos[index + distance] = 1;
              break;
            } else if (i >= fieldSize) {
              bugPos[index] = 0;
              break;
            }
          }
        }
      }
    } else {
      if (index - distance < fieldSize - 1) {
        bugPos[index] = 0;
      } else if (element[index - distance] === 0) {
        bugPos[index] = 0;
        bugPos[index - distance] = 1;
      } else {
        for (let i = index - distance + 1; i > 0; i++) {
          if (bugPos[i] === 0) {
            bugPos[index] = 0;
            bugPos[index - distance] = 1;
            break;
          } else if (i <= fieldSize) {
            bugPos[index] = 0;
            break;
          }
        }
      }
    }
  });

  function replaceBug(arr, oldIndex, newIndex) {
    arr[oldIndex] = 0;
    arr[newIndex] = 1;
  }
  console.log(bugPos);
}
// fix field size, doesn't work
ladyBugs([3, "0 1", "0 right 1", "2 right 1"]);
ladyBugs([3, "0 1 2", "0 right 1", "1 right 1", "2 right 1"]);
ladyBugs([5, "3", "3 left 2", "1 left -2"]);
