const User = require('../models/user');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const { secret, saltRounds } = require('../config/config');

exports.register = async ({ username, password, repass }) => {
	if (password !== repass) {
		return false;
	}

	const hashedPassword = await bcrypt.hash(password, saltRounds);

	let createdUser = User.create({
		username,
		password: hashedPassword,
	});

	return createdUser;
};

exports.login = async ({ username, password }) => {
	const user = await User.findOne({ username });
	if (!user) {
		return false;
	}

	const isMatched = await bcrypt.compare(password, user.password);
	// can also use promisify from utils
	if (!isMatched) {
		throw {
			message: 'Credentials invalid'
		}
	}
	if (isMatched) {
		let authToken = new Promise((resolve, reject) => {
			jwt.sign(
				{ _id: user._id, username: user.username },
				secret,
				{ expiresIn: '2d' },
				(err, token) => {
					if (err) {
						reject(err);
					}
					resolve(token);
				}
			);
		});
		return authToken;
	}
	return false;
};
