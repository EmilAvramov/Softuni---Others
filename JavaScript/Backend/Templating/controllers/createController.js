const uniqid = require('uniqid')
const cubeService = require('../services/cubeService')

exports.view = (req, res) => {
	res.render('create');
};

exports.create = (req, res) => {
	let cube = req.body;
	if (cube.name.length < 2) {
		return res.status(400).send('Invalid Request');
	}
    cube.id = uniqid()
    cubeService.save(cube)
    res.redirect('/')
};
