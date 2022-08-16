const Item = require('../models/item');

async function getAll() {
	return Item.find({});
}

async function create(item) {
	const result = Item.create({
		make: item.make,
		model: item.model,
		year: item.year,
		description: item.description,
		price: item.price,
		img: item.img,
		material: item.material,
	});

	return result;
}

async function getById(id) {
	return Item.findById(id);
}

async function updateById(id, item) {
	const exists = await Item.findById(id);

	if (exists) {
		exists.make = item.make;
		exists.model = item.model;
		exists.year = item.year;
		exists.description = item.description;
		exists.price = item.price;
		exists.img = item.img;
		exists.material = item.material;
		await exists.save();
		return exists;
	} else {
		const error = new Error('Not Found');
		error._notFound = true;
		throw error;
	}
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
