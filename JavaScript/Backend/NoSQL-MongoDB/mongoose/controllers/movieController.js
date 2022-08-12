const { Movie } = require('../models/Movie');

exports.view = async (req, res) => {
	const movies = await Movie.find().lean();
	// movies.forEach((movie) => {
	// 	console.log(movie.getInfo());
	// 	console.log(movie.isNew);
	// });
	res.render('movies', { movies });
};

exports.create = async (req, res) => {
	await Movie.create(req.body);
	res.redirect('/movies');
};

exports.details = async (req, res) => {
	// let movie = await Movie.findOne({ _id: req.params.id }).lean();
	let movie = await Movie.findById(req.params.id).lean();
	res.render('details', { movie });
};
