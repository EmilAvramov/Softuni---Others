const cubes = require('./../config/database.json');
const fs = require('fs');
const path = require('path')

exports.save = (cube) => {
    cubes.push(cube);
    return fs.writeFile(
		path.resolve('../Templating/config/database.json'),
		JSON.stringify(cubes, '', 4),
		(err) => {
			if (err) console.log('Error', err);
		}
	)
}