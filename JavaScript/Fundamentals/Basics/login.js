function login(list) {
  var username = list[0];
  list.shift();
  var attempts = list;
  let counter = 0;
  attempts.forEach((attempt) => {
    if (username === attempt.split("").reverse().join("")) {
      console.log(`User ${username} logged in.`);
    } else {
      counter += 1;
      if (counter === 4) {
        console.log(`User ${username} blocked!`);
      } else {
        console.log("Incorrect password. Try again.");
      }
    }
  });
}

login(["Acer", "login", "go", "let me in", "recA"]);
