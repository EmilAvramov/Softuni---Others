function replace(string1, missing, string2) {
  var newStr = string1.replace("_", missing);
  if (newStr === string2) {
    console.log("Matched");
  } else {
    console.log("Not Matched");
  }
}

replace("Str_ng", "I", "Strong");
replace("Str_ng", "i", "String");
