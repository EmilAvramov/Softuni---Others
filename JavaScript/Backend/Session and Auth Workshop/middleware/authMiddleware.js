const jwt = require('jsonwebtoken');
const { promisify } = require('util');
const { sessionName, secret } = require('../config/config');

const jwtPromise = promisify(jwt.verify);

exports.auth = async (req, res, next) => {
	let token = req.cookies[sessionName];

	if (token) {
		try {
			let decodedToken = await jwtPromise(token, secret);
			req.user = decodedToken;
			res.locals.user = decodedToken
		} catch (e) {
			return false;
		}
	}
	next();
};

exports.isAuth = (req, res, next) => {
	if (!req.user) {
		return res.render('404');
	}
	next();
};
