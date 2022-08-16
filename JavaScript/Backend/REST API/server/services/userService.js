const User = require('../models/user');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const jwtSecret = '902713-091u293jdiwndka';

async function createSession(user) {
	const payload = {
		email: user.email,
		_id: user._id,
	};

	const accessToken = jwt.sign(payload, jwtSecret);

	return {
		email: user.email,
		accessToken,
		_id: user._id,
	};
}

async function register(email, password) {
	const existing = await User.findOne({ email: new RegExp(`^${email}$`, 'i') });

	if (existing) {
		throw new Error('Email is taken');
	}

	const hashedPassword = await bcrypt.hash(password, 10);
	const user = await User.create({
		email,
		hashedPassword,
	});

	return createSession(user);
}

async function login(email, password) {}

module.exports = {
	register,
	login,
};
