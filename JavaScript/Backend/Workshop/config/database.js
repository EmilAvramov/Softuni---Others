const mongoose = require('mongoose');

const connString = 'mongodb://localhost:27017/cubicle';

exports.initDatabase = () => mongoose.connect(connString);
