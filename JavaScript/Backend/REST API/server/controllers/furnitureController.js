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
	res.json(await getAll());
});

router.post('/', async (req, res) => {
	const item = {
		make: req.body.make,
		model: req.body.model,
		year: req.body.year,
		description: req.body.description,
		price: req.body.price,
		img: req.body.img,
		material: req.body.material,
	};

	try {
		const result = await create(item);
		res.json(result);
	} catch (e) {
		const message = errorMapper(e)
		res.status(400).json({message});
	}
});

router.get('/:id', async (req, res) => {
	const id = req.params.id;
	const item = await getById(id);

	if (item) {
		res.json(item);
	} else {
		res.status(404).json({ message: `item ${id} not found` });
	}
});

router.put('/:id', async (req, res) => {
	const item = {
		make: req.body.make,
		model: req.body.model,
		year: req.body.year,
		description: req.body.description,
		price: req.body.price,
		img: req.body.img,
		material: req.body.material,
	};

	try {
		const result = await updateById(req.params.id, item);
		res.json(result);
	} catch (e) {
		if (err._notFound) {
			res.status(404).json({ message: `item ${id} not found` });
		} else {
			res.status(400).json({ message: 'Request Error' });
		}
	}
});

router.delete('/:id', async (req, res) => {
	try {
		const result = await deleteById(req.params.id);
		res.json(result);
	} catch (e) {
		res.status(400).json({ message: 'Not Found' });
		
	}
})

module.exports = router;
