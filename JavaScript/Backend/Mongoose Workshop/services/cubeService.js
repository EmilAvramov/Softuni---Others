const Cube = require('../models/cube');

exports.create = (cube) => Cube.create(cube)

exports.getOne = (id) => {
	return Cube.findById(id);
};

exports.getAll = async (searchInput, fromInput, toInput) => {
	let cubes = await Cube.find().lean()
	return cubes
	// const search = searchInput || '';
	// const from = Number(fromInput) || 0;
	// const to = Number(toInput) || 6;

	// return cubes
	// 	.filter((x) => x.name.toLowerCase().includes(search.toLowerCase()))
	// 	.filter(
	// 		(x) =>
	// 			x.difficultyLevel >= Number(from) &&
	// 			x.difficultyLevel <= Number(to)
	// 	);
};
