const Accessory = require('../models/accessory');
const Cube = require('../models/cube');

exports.create = (cube) => Cube.create(cube);

exports.getOne = (id) => Cube.findById(id);
exports.getOneDetailed = (id) => Cube.findById(id).populate('accessories');

exports.getAll = async (search, fromInput, toInput) => {
	const from = Number(fromInput) || 0;
	const to = Number(toInput) || 6;

	const cubes = await Cube.find({
		name: { $regex: new RegExp(search, 'i') },
	})
		.where('difficultyLevel')
		.lte(to)
		.gte(from)
		.lean();

	return cubes;
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

exports.edit = async (id, data) =>
	Cube.findByIdAndUpdate(id, data);

exports.delete = (id) => Cube.findByIdAndDelete(id);
