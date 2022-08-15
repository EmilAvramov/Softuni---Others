const express = require('express');
const handlebars = require('express-handlebars');
const router = require('./router');
const cookieParser = require('cookie-parser');
const { auth } = require('../middleware/authMiddleware');
const { errorHandler } = require('../middleware/errorHandleMiddleware');

const app = express();

app.engine(
	'hbs',
	handlebars.engine({
		extname: 'hbs',
	})
);
app.set('view engine', 'hbs');
app.use(express.static('static'));
app.use(cookieParser());
app.use(express.urlencoded({ extended: false }));
app.use(auth);
app.use(router);
app.use(errorHandler);

module.exports = app;
