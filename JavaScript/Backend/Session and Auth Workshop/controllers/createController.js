const cubeService = require('../services/cubeService');
const accessoryService = require('../services/accessoryService');

exports.viewCube = (req, res) => {
	res.render('items/createCube');
};

exports.viewAccessory = (req, res) => {
	res.render('items/createAccessory');
};

exports.createCube = (req, res) => {
	const cube = req.body;
	cube.owner = req.user._id;
	cubeService.create(cube);
	res.redirect('/');
};

exports.createAccessory = (req, res) => {
	accessoryService.create(req.body);
	res.redirect('/');
};
