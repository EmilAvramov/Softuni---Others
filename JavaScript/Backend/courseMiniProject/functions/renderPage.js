const fs = require('fs/promises');

exports.render = async (res, path) => {
	let addBreed = await fs.readFile(path, 'utf-8');
	res.write(addBreed);
};
