const express = require('express');
const hbs = require('express-handlebars');
const mongoose = require('mongoose');
const router = require('./config/router');

const app = express();
const url = 'mongodb://localhost:27017/Movies';
mongoose
	.connect(url)
	.then(() => console.log('Mongoose connected'))
	.catch((err) => console.log(err));

app.engine(
	'hbs',
	hbs.engine({
		extname: 'hbs',
	})
);

app.set('view engine', 'hbs');
app.use(express.urlencoded({ extended: false }));
app.use(router)

app.listen(5000, () => console.log('Server listening to port 5000...'));
