function dunDark(string) {
  let health = 100;
  let coins = 0;
  let rooms = string[0].split("|");
  let killed = false;
  rooms.every((element, index) => {
    if (killed) {
      return false;
    }
    element = element.split(" ");
    element[1] = Number(element[1]);
    if (element[0] === "potion") {
      if (element[1] + health > 100) {
        console.log(`You healed for ${100 - health} hp.`);
        health = 100;
      } else {
        health += element[1];
        console.log(`You healed for ${element[1]} hp.`);
      }
      console.log(`Current health: ${health} hp.`);
    } else if (element[0] === "chest") {
      coins += element[1];
      console.log(`You found ${element[1]} coins.`);
    } else {
      if (element[1] < health) {
        health -= element[1];
        console.log(`You slayed ${element[0]}.`);
      } else {
        console.log(`You died! Killed by ${element[0]}.`);
        console.log(`Best room: ${index + 1}`);
        killed = true;
      }
    }
    return true;
  });
  if (!killed) {
    console.log("You've made it!");
    console.log(`Coins: ${coins}`);
    console.log(`Health: ${health}`);
  }
}

dunDark(["rat 10|bat 20|potion 10|rat 10|chest 100|boss 70|chest 1000"]);
dunDark(["cat 10|potion 30|orc 10|chest 10|snake 25|chest 110"])