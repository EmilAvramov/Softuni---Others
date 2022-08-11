const fs = require('fs');

const readStream = fs.createReadStream(
	'./JavaScript/backend/streams/largefile.txt'
);
const writeStream = fs.createWriteStream(
	'./JavaScript/backend/streams/copyFile.txt',
	{ encoding: 'utf-8' }
);

readStream.on('data', (chunk) => {
	console.log(chunk);
	console.log('-----------------------');
});

readStream.on('end', () => {
	console.log('Finished');
});


writeStream.on('finish', () => console.log('file is saved'))

writeStream.write('Hello World')
writeStream.write('\n')
writeStream.write('I\'m alive')
writeStream.end()