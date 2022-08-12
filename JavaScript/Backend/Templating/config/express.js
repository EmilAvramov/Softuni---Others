const express = require('express');
const handlebars = require('express-handlebars');
const routes = require('./routes')

const app = express();

app.engine(
	'hbs',
	handlebars.engine({
		extname: 'hbs',
	})
);
app.set('view engine', 'hbs');
app.use(express.static('static'));
app.use(express.urlencoded({extended:false}))
app.use(routes)

module.exports = app