const mongoose = require('mongoose');

const cubeSchema = new mongoose.Schema({
	id: mongoose.Types.ObjectId,
	name: {
		type: String,
		required: [true, 'This field is required'],
	},
	description: {
		type: String,
		required: [true, 'This field is required'],
		maxLength: 120,
	},
	imageUrl: {
		type: String,
		required: [true, 'This field is required'],
		validate: {
			validator: function() {
                return this.imageUrl.startsWith('http')
            },
			message: 'Image url should be link',
		},
	},
	difficultyLevel: {
		type: Number,
		required: [true, 'This field is required'],
		min: 1,
		max: 6,
	},
	// accessories: {
	// 	ObjectId: mongoose.Types.ObjectId,
	// 	ref: ReferenceError,
	// },
});

const Cube = mongoose.model('Cube', cubeSchema)

module.exports = Cube;