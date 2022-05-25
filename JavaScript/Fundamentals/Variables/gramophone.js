function gramophone(band, album, song) {
  const songDuration = (album.length * band.length * song.length) / 2;
  let count = 0;
  count = songDuration / 2.5;
  console.log(`The plate was rotated ${Math.ceil(count)} times.`);
}

gramophone("Black Sabbath", "Paranoid", "War Pigs");
