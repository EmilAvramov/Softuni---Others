const authService = require('../services/authService');
const router = require('express').Router()
const { sessionName } = require('../config/config');
const { isAuth } = require('../middleware/authMiddleware');

router.get('/register', (req, res) => {
	res.render('auth/register');
});

router.post('/register', async (req, res) => {
	let createUser = await authService.register(req.body);
	if (createUser) {
		res.redirect('/auth/login');
	} else {
		res.redirect('/404');
	}
});

router.get('/login', (req, res) => {
	res.render('auth/login');
});

router.post('/login', async (req, res) => {
	const token = await authService.login(req.body);
	if (!token) {
		res.redirect('/404');
	}

	res.cookie(sessionName, token, { httpOnly: true });
	res.redirect('/');
});

router.use(isAuth);

router.get('/logout', (req, res) => {
	res.clearCookie(sessionName);
	res.redirect('/');
});

module.exports = router