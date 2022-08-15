const router = require('express').Router();
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

router.post(
	'/cube',
	body('name', 'Name is required').not().isEmpty(),
	body('description', 'Length is wrong').isLength({ min: 5, max: 120 }),
	body('difficultyLevel', 'Needs to be 1 to 6')
		.toInt()
		.isInt({ min: 1, max: 6 }),
	(req, res) => {
		const cube = req.body;
		cube.owner = req.user._id;

		const errors = validationResult(req);

		if (!errors.isEmpty()) {
			return res.status(400).send(errors.array()[0].msg);
		}

		cubeService.create(cube);
		res.redirect('/');
	}
);

router.post('/accessory', (req, res) => {
	accessoryService.create(req.body);
	res.redirect('/');
});

module.exports = router;
