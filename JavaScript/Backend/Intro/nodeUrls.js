const url = require('url');

// Legacy
const oldurl = url.parse('https://gameblob.herokuapp.com');

// New Syntax
const newurl = new URL('https://gameblob.herokuapp.com');

console.log(newurl)
console.log(oldurl)