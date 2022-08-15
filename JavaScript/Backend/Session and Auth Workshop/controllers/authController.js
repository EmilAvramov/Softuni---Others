const authService = require('../services/authService');

exports.registerView = (req, res) => {
	res.render('auth/register');
};

exports.registerPost = async (req, res) => {
	let createUser = await authService.register(req.body);
	if (createUser) {
		res.redirect('/login');
	} else {
		res.redirect('404');
	}
};

exports.loginView = (req, res) => {
	res.render('auth/login');
};

exports.loginPost = async (req, res) => {
	const token = await authService.login(req.body);
	if (!token) {
		res.redirect('404');
	}

    res.cookie('session', token)
    res.redirect('/')
};

exports.logout = (req, res) => {
	res.redirect('/');
};
