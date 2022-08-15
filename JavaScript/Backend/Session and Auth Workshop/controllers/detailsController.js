const cubeService = require('../services/cubeService');
const accessoryService = require('../services/accessoryService');

exports.view = async (req, res) => {
	const cube = await cubeService.getOneDetailed(req.params.id).lean();
	res.render('items/details', { cube });
};

exports.attachView = async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();

	console.log(cube.owner)
	console.log(req.user._id)

	if (cube.owner != req.user._id) {
		return res.redirect('/404');
	}

	const accessories = await accessoryService.filter(cube.accessories).lean();
	res.render('items/attach', { cube, accessories });
};

exports.attachPost = async (req, res) => {
	const accessoryId = req.body.accessory;
	await cubeService.attach(req.params.id, accessoryId);
	res.redirect(`items/details/${req.params.id}`);
};

exports.editView = async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();

	if (cube.owner != req.user._id) {
		return res.redirect('/404');
	}

	if (!cube) {
		res.render('404');
	}
	res.render('items/editCube', { cube });
};

exports.editPost = async (req, res) => {
	let modified = await cubeService.edit(req.params.id, req.body);
	res.redirect(`/details/${modified._id}`);
};
