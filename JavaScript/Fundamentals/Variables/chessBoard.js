function chess(number) {
  var header = '<div class="chessboard">';
  var open = "  <div>";
  var close = "  </div>";
  var elementBlack = '   <span class="black"></span>';
  var elementWhite = '   <span class="white"></span>';
  var footer = "</div>";
  console.log(header);
  for (let i = 1; i <= number; i++) {
    if (i % 2 !== 0) {
      console.log(open);
      for (let j = 1; j <= number; j++) {
        if (j % 2 !== 0) {
          console.log(elementBlack);
        } else {
          console.log(elementWhite);
        }
      }
    } else {
      console.log(open);
      for (let j = 1; j <= number; j++) {
        if (j % 2 !== 0) {
          console.log(elementWhite);
        } else {
          console.log(elementBlack);
        }
      }
    }
    console.log(close);
  }
  console.log(footer);
}

chess(6);
