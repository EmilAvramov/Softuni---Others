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

cubeSchema.path('imageUrl').validate(function () {
	return this.imageUrl.startsWith('http');
}, 'Image url should be a link');


const Cube = mongoose.model('Cube', cubeSchema)

module.exports = Cube;