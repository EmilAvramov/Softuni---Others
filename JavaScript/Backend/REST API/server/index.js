const express = require('express');
const mongoose = require('mongoose');
const cors = require('./middlewares.js/cors');
const furnitureController = require('./controllers/furnitureController');
const userController = require('./controllers/userController');

async function start() {
	try {
		await mongoose.connect('mongodb://localhost:27017/furniture');
		console.log('Database ready');
	} catch (err) {
		console.log('Error connecting to database');
		return process.exit(1);
	}

	const app = express();

	app.use(express.json());
	app.use(cors());
	app.use('/data/catalog', furnitureController);
	app.use('/users', userController);

	app.listen(3030, () => console.log('Server listening to port 3030...'));
}

start();
