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

const User = mongoose.model('User', userSchema);

module.exports = User;
