const Accessory = require('../models/accessory');
const Cube = require('../models/cube');

exports.create = (cube) => Cube.create(cube);

exports.getOne = (id) => Cube.findById(id).populate('accessories');

exports.getAll = async (searchInput, fromInput, toInput) => {
	let cubes = await Cube.find().lean();
	return cubes;
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

exports.attach = async (cubeId, accessoryId) => {
	const cube = await Cube.findById(cubeId);
	const accessory = await Accessory.findById(accessoryId);

	cube.accessories.push(accessory);
	accessory.cubes.push(cube);

	await cube.save();
	await accessory.save();

	return [cube, accessory];
};
