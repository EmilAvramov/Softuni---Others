function games(arr) {
  function isInstalled(game) {
    if (installed.includes(game)) {
      return true;
    } else {
      return false;
    }
  }

  let installed = arr.shift().split(" ");

  for (let i = 0; i < arr.length; i++) {
    if (arr[i] === "Play!") {
      break;
    } else {
      let command, game, expansion;
      [command, game] = arr[i].split(" ");
      if (!isInstalled(game)) {
        if (command === "Install") {
          installed.push(game);
        } else if (command === "Expansion") {
          expansion = game.split("-")[1];
          game = game.split("-")[0];
          if (installed.includes(game)) {
            installed.splice(
              installed.indexOf(game) + 1,
              0,
              game + ":" + expansion
            );
          }
        }
      } else if (isInstalled(game)) {
        if (command === "Uninstall") {
          installed.splice(installed.indexOf(game), 1);
        } else if (command === "Update") {
          installed.splice(installed.indexOf(game), 1);
          installed.push(game);
        }
      }
    }
  }
  console.log(installed.join(" "));
}

games([
  "CS WoW Diablo",
  "Install LoL",
  "Uninstall WoW",
  "Update Diablo",
  "Expansion CS-Go",
  "Play!",
]);
