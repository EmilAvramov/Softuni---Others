const { isAuth, isOwner } = require('../middlewares/guards');
const preload = require('../middlewares/preload');

const {
	getAll,
	create,
	getById,
	updateById,
	deleteById,
} = require('../services/furnitureService');
const errorMapper = require('../utils/errorMapper');

const router = require('express').Router();

router.get('/', async (req, res) => {
	res.json(await getAll(req.query.where));
});

router.post('/', isAuth(), async (req, res) => {
	const item = {
		make: req.body.make,
		model: req.body.model,
		year: req.body.year,
		description: req.body.description,
		price: req.body.price,
		img: req.body.img,
		material: req.body.material,
		_ownerId: req.user._id,
	};

	try {
		const result = await create(item);
		res.json(result);
	} catch (e) {
		const message = errorMapper(e);
		res.status(400).json({ message });
	}
});

router.get('/:id', preload(), async (req, res) => {
	res.json(res.locals.item);
});

router.put('/:id', preload(), isOwner(), async (req, res) => {
	try {
		const result = await updateById(res.locals.item, req.body);
		res.json(result);
	} catch (e) {
		if (err._notFound) {
			res.status(400).json({ message: 'Request Error' });
		}
	}
});

router.delete('/:id', isAuth(), isOwner(), async (req, res) => {
	try {
		const result = await deleteById(req.params.id);
		res.json(result);
	} catch (e) {
		res.status(400).json({ message: 'Not Found' });
	}
});

module.exports = router;
