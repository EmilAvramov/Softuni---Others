const { validateToken } = require('../services/userService');

module.exports = () => (req, res, next) => {
	const token = req.headers['x-authorization'];

	if (token) {
		try {
			const payload = validateToken(token);
            req.user = {
                email: payload.email,
                _id: payload._id,
                token
            }

		} catch (e) {
			return res
				.status(401)
				.json({ message: 'Invalid access token, please relogin' });
		}
	}

	next();
};
