const mongoose = require('mongoose');

const movieSchema = new mongoose.Schema({
	title: {
		type: String,
		required: [true, 'This is required'],
		minLength: 2,
		maxLength: 30,
	},
	imageUrl: {
		type: String,
		enum: ['list1', 'list2', 'list3']
	},
	year: {
		type: Number,
		min: [1990, 'Year should be higher than {VALUE}']
	},
});

movieSchema.methods.getInfo = function () {
	return `${this.title} - ${this.imageUrl} - ${this.year}`;
};

movieSchema.virtual('isNew').get(function () {
	return this.year >= 2020;
});

movieSchema.path('title').validate(function () {
	return this.title.length >= 2 && this.title.length <= 20;
}, 'This movie should be correct');

const Movie = mongoose.model('Movie', movieSchema);

exports.Movie = Movie;
