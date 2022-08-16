const { register, login, logout } = require('../services/userService');

const router = require('express').Router();

router.post('/register', async (req, res) => {
	const { email, password } = req.body;

	try {
		const result = await register(email, password);
		res.status(201).json(result);
	} catch (e) {
		res.status(400).json({ message: e.message });
	}
});

router.post('/login', async (req, res) => {
	const { email, password } = req.body;

	try {
		const result = await login(email, password);
		res.status(200).json(result);
	} catch (e) {
		res.status(400).json({ message: e.message });
	}
});

router.get('/logout', (req, res) => {
	logout(req.user.accessToken);
	res.status(204).end();
});

module.exports = router;
