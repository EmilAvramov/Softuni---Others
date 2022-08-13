const Accessory = require('../models/accessory');

exports.create = (accessory) => Accessory.create(accessory);

exports.getAll = async () => {
	const accessories = await Accessory.find().lean();
	return accessories;
};