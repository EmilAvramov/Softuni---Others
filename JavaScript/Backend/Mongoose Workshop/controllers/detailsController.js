const cubeService = require('../services/cubeService');

exports.view = async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();
	res.render('details', { cube });
};
