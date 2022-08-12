const { Movie } = require('../models/Movie');

exports.view = async (req, res) => {
	const movies = await Movie.find().lean();
	res.render('movies', { movies });
};

exports.create = async (req, res) => {
    console.log(req.body)
}