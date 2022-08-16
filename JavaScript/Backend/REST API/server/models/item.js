const { model, Schema } = require('mongoose');

const itemSchema = new Schema({
	make: { type: String, minLength: 4 },
	model: { type: String },
	year: {
		type: Number,
		min: [1950, 'Year should be after 1950'],
		max: [2050, 'Year must be before 2050'],
	},
	description: { type: String },
	price: { type: Number, min: [0.01, 'Price must be a positive number'] },
	img: { type: String },
	material: { type: String },
});

const Item = model('Item', itemSchema);

module.exports = Item;
