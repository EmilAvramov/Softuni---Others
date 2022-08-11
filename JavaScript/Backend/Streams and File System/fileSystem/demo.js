const fs = require('fs');

// const text = fs.readFileSync('./JavaScript/backend/fileSystem//lorem.txt', {
// 	encoding: 'utf-8'
// });
// console.log(text)

fs.readFile('./JavaScript/backend/fileSystem//lorem.txt', {
	encoding: 'utf-8'
}, (err, data) => {
    if (err) {
        return
    }
    console.log(data)
});

console.log('end')