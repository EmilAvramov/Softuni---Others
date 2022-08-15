const router = require('express').Router()
const { isAuth } = require('../middleware/authMiddleware');
const cubeService = require('../services/cubeService');
const accessoryService = require('../services/accessoryService');
const { body, validationResult } = require('express-validator');

router.use(isAuth);

router.get('/cube', (req, res) => {
	res.render('items/createCube');
});

router.get('/accessory', (req, res) => {
	res.render('items/createAccessory');
});

router.post('/cube', (req, res) => {
	const cube = req.body;
	cube.owner = req.user._id;
	cubeService.create(cube);
	res.redirect('/');
});

router.post('/accessory', (req, res) => {
	accessoryService.create(req.body);
	res.redirect('/');
});

module.exports = router