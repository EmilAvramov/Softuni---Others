const cubes = require('./../config/database.json');
const fs = require('fs');
const path = require('path');

exports.save = (cube) => {
	cubes.push(cube);
	return fs.writeFile(
		path.resolve('../Templating/config/database.json'),
		JSON.stringify(cubes, '', 4),
		(err) => {
			if (err) console.log('Error', err);
		}
	);
};

exports.getOne = (id) => {
	return cubes.filter((x) => x.id == id);
};

exports.getAll = (searchInput, fromInput, toInput) => {
	const search = searchInput || ''
	const from = Number(fromInput) || 0
	const to = Number(toInput) || 6

	return cubes
		.filter((x) => x.name.toLowerCase().includes(search.toLowerCase()))
		.filter(
			(x) =>
				x.difficultyLevel >= Number(from) &&
				x.difficultyLevel <= Number(to)
		);
};
