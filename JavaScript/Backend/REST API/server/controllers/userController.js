const { register } = require('../services/userService');

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

module.exports = router