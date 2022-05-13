function pyramid(width, increment) {
  var floors = 0;
  var stoneBlocks = 0;
  var marbleBlocks = 0;
  var lapisBlocks = 0;
  var goldBlocks = 0;
  for (let i = width; i > 0; i -= 2) {
    floors += 1;
    if (i - increment * 2 > 0) {
      stoneBlocks += (i - 1 * 2) * (i - 1 * 2);
    }
    if (floors % 5 !== 0 && i > 2) {
      marbleBlocks += i * 4 - 4;
    } else if (floors % 5 === 0 && i > 2) {
      lapisBlocks += i * 4 - 4;
    }
    if (i <= 2) {
      goldBlocks += i * i;
    }
  }
  console.log(`Stone required: ${Math.ceil(stoneBlocks * increment)}`);
  console.log(`Marble required: ${Math.ceil(marbleBlocks * increment)}`);
  console.log(`Lapis Lazuli required: ${Math.ceil(lapisBlocks * increment)}`);
  console.log(`Gold required: ${Math.ceil(goldBlocks * increment)}`);
  console.log(`Final pyramid height: ${Math.floor(floors * increment)}`);
}

pyramid(20, 1);
