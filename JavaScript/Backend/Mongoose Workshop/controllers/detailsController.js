const cubeService = require('../services/cubeService');
const accessoryService = require('../services/accessoryService');

exports.view = async (req, res) => {
	const cube = await cubeService.getOneDetailed(req.params.id).lean();
	res.render('details', { cube });
};

exports.attachView = async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();
	const accessories = await accessoryService.filter(cube.accessories).lean();
	res.render('attach', { cube, accessories });
};

exports.attachPost = async (req, res) => {
	const accessoryId = req.body.accessory;
	await cubeService.attach(req.params.id, accessoryId);
	res.redirect(`/details/${req.params.id}`);
};
