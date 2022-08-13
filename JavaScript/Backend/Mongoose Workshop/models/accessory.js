const mongoose = require('mongoose');

const accessorySchema = new mongoose.Schema({
	id: mongoose.Types.ObjectId,
	name: {
		type: String,
		required: [true, 'This field is required'],
	},
	imageUrl: {
		type: String,
		required: [true, 'This field is required'],
		validate: {
			validator: function () {
				return this.imageUrl.startsWith('http');
			},
			message: 'Image url should be link',
		},
	},
	description: {
		type: String,
		required: [true, 'This field is required'],
		maxLength: 120,
	},
	cubes: [
		{
			type: mongoose.Types.ObjectId,
			ref: 'Cube',
		},
	],
});

const Accessory = mongoose.model('Accessory', accessorySchema);

module.exports = Accessory;
