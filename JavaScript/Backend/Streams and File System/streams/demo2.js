const fs = require('fs');
const zlib = require('zlib')

const readStream = fs.createReadStream(
	'./JavaScript/backend/streams/largefile.txt',
	{ highWaterMark: 1024 }
);
const writeStream = fs.createWriteStream(
	'./JavaScript/backend/streams/copyFile.txt',
	{ encoding: 'utf-8' }
);

const gzip = zlib.createGzip()

// readStream.on('data', (chunk) => {
// 	writeStream.write(chunk);
// });

// readStream.on('end', () => {
// 	writeStream.end();
// 	console.log('Finished');
// });

writeStream.on('finish', () => console.log('file is saved'));

readStream.pipe(gzip).pipe(writeStream);
