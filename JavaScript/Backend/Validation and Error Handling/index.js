const express = require('express');
const hbs = require('express-handlebars');

const app = express();

app.engine('hbs', hbs.engine({ extname: 'hbs' }));
app.set('view engine', 'hbs');
app.use(express.static('static'));
app.use(express.urlencoded({ extended: false }));

app.listen(5000, () => console.log('Server listening to port 5000...'));
