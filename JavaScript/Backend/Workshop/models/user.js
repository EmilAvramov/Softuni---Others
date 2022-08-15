const mongoose = require('mongoose');


const userSchema = new mongoose.Schema({
	username: {
		type: String,
		required: [true, 'This field is required'],
	},
	password: {
		type: String,
		required: [true, 'This field is required'],
	},
});

// Model validations
// const bcrypt = require('bcrypt');
// const { saltRounds } = require('../config/config');
// userSchema.virtual('repass').set(function (value) {
// 	if (this.password !== value) {
// 		throw new Error('Passwords must match');
// 	}
// });

// userSchema.pre('save', function (next) {
// 	bcrypt.hash(this.password, saltRounds).then((hashed) => {
// 		this.password = hashed;

// 		next();
// 	});
// });

const User = mongoose.model('User', userSchema);

module.exports = User;
