const jwt = require('jsonwebtoken');
const { promisify } = require('util');
const { sessionName, secret } = require('../config/config');

const jwtPromise = promisify(jwt.verify);

exports.auth = async (req, res, next) => {
	let token = req.cookies[sessionName];

	if (token) {
		try {
			let decodedToken = await jwtPromise(token, secret);
            req.user = decodedToken
		} catch (e) {
			return false;
		}
	}
	next();
};
