const mongoose = require('mongoose');

const movieSchema = new mongoose.Schema({
	title: String,
	imageurl: String,
	year: Number,
});

const Movie = mongoose.model('Movie', movieSchema)

exports.Movie = Movie