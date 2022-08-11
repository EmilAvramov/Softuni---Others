const fs = require('fs');
const fsPromises = require('fs/promises')

fs.readdir('./javascript', (err, data) => {
    if (err) {
        return
    }
    console.log(data)
})

fsPromises.mkdir('test').then(console.log('finished'))