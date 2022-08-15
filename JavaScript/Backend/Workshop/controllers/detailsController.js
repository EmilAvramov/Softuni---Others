const router = require('express').Router()
const { isAuth } = require('../middleware/authMiddleware');
const cubeService = require('../services/cubeService');
const accessoryService = require('../services/accessoryService');

router.get('/:id/details', async (req, res) => {
	const cube = await cubeService.getOneDetailed(req.params.id).lean();
	const isOwner = cube.owner == req.user?._id;
	res.render('items/details', { cube, isOwner });
});

router.use(isAuth);

router.get('/:id/attach', async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();

	if (cube.owner != req.user._id) {
		return res.redirect('/404');
	}

	const accessories = await accessoryService.filter(cube.accessories).lean();
	res.render('items/attach', { cube, accessories });
});

router.post('/:id/attach', async (req, res) => {
	const accessoryId = req.body.accessory;
	await cubeService.attach(req.params.id, accessoryId);
	res.redirect(`/cube/${req.params.id}/details/`);
});

router.get('/:id/edit', async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();

	if (cube.owner != req.user._id) {
		return res.redirect('/404');
	}

	if (!cube) {
		res.render('404');
	}
	res.render('items/editCube', { cube });
});

router.post('/:id/edit', async (req, res) => {
	let modified = await cubeService.edit(req.params.id, req.body);
	res.redirect(`/cube/${modified._id}/details/`);
});

router.get('/:id/delete', async (req, res) => {
	const cube = await cubeService.getOne(req.params.id).lean();

	res.render(`items/deleteCube`, { cube });
});

router.post('/:id/delete', async (req, res) => {
	await cubeService.delete(req.params.id);

	res.redirect('/');
});

module.exports = router