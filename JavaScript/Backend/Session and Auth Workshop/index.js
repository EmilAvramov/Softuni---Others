const env = process.env.NODE_ENV || 'development';

const config = require('./config/config')[env];
const app = require('./config/express');
const { initDatabase } = require('./config/database');

initDatabase()
	.then(() => {
		app.listen(
			config.port,
			console.log(`Listening on port ${config.port}...`)
		);
	})
	.catch((err) => {
		console.log('Cannot connect to db');
	});
