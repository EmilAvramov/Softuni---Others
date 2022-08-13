const cubeService = require('../services/cubeService');

exports.view = async (req, res) => {
	let { search, from, to } = req.query;
	const cubes = await cubeService.getAll(search, from, to);
	res.render('index', { cubes });
};
