function miningCoins(shifts) {
  let coinsBought = 0;
  let firstDay = 0;
  var money = 0;
  const goldValue = 67.51;
  const bitcoinValue = 11949.16;
  for (let i = 0; i < shifts.length; i++) {
    if ((i + 1) % 3 === 0) {
      money += shifts[i] * goldValue * 0.7;
    } else {
      money += shifts[i] * goldValue;
    }

    while (money >= bitcoinValue) {
      coinsBought++;
      money -= bitcoinValue;
      if (firstDay === 0) {
        firstDay = i + 1;
      }
    }
  }
  console.log(`Bought bitcoins: ${coinsBought}`);
  if (firstDay !== 0) {
    console.log(`Day of the first purchased bitcoin: ${firstDay}`);
  }
  console.log(`Left money: ${money.toFixed(2)} lv.`);
}

miningCoins([100, 200, 300]);
