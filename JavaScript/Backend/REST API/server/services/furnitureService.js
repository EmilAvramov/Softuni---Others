const Item = require('../models/item');

async function getAll(query) {
	if (query) {
		const userId = query.split('=')[1].slice(1, -1);
		return Item.find({ _ownerId: userId });
	}
	return Item.find();
}

async function create(item) {
	const result = await Item.create({
		make: item.make,
		model: item.model,
		year: item.year,
		description: item.description,
		price: item.price,
		img: item.img,
		material: item.material,
		_ownerId: item._ownerId,
	});

	return result;
}

async function getById(id) {
	return Item.findById(id);
}

async function updateById(exists, item) {
	exists.make = item.make;
	exists.model = item.model;
	exists.year = item.year;
	exists.description = item.description;
	exists.price = item.price;
	exists.img = item.img;
	exists.material = item.material;
	await exists.save();
	return exists;
}

async function deleteById(id) {
	return await Item.findByIdAndDelete(id);
}

module.exports = {
	getAll,
	create,
	getById,
	updateById,
	deleteById,
};
