const User = require('../models/user');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const jwtSecret = '902713-091u293jdiwndka';
const blackList = new Set();

async function createSession(user) {
	const payload = {
		email: user.email,
		_id: user._id,
	};

	const accessToken = jwt.sign(payload, jwtSecret, {
		expiresIn: '2d',
	});

	return {
		email: user.email,
		accessToken: accessToken,
		_id: user._id,
	};
}

async function register(email, password) {
	const existing = await User.findOne({
		email: new RegExp(`^${email}$`, 'i'),
	});

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

async function login(email, password) {
	const user = await User.findOne({
		email: new RegExp(`^${email}$`, 'i'),
	});

	if (!user) {
		throw new Error('Incorrect credentials');
	}

	const match = await bcrypt.compare(password, user.hashedPassword);

	if (!match) {
		throw new Error('Incorrect credentials');
	}

	return createSession(user);
}

function validateToken(token) {
	if (blackList.has(token)) {
		throw new Error('Token is blacklisted');
	}
	return jwt.verify(token, jwtSecret);
}

function logout(token) {
	blackList.add(token);
}

module.exports = {
	register,
	login,
	validateToken,
	logout,
};
