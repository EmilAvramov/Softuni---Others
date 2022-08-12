const cubeService = require('../services/cubeService');

exports.view = (req, res) => {
	let { search, from, to } = req.query;
	const cubes = cubeService.getAll(search, from, to);
	res.render('index', { cubes });
};
