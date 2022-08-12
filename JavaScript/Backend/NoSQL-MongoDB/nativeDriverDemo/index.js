const express = require('express');
const hbs = require('express-handlebars');
const { MongoClient } = require('mongodb');

const app = express();
const url = 'mongodb://localhost:27017';
const client = new MongoClient(url);

client.connect().then(() => console.log('MongoDB connected'));

const db = client.db('Movies');
const movieCollection = db.collection('Movies');

app.engine(
	'hbs',
	hbs.engine({
		extname: 'hbs',
	})
);

app.set('view engine', 'hbs');

app.get('/', (req, res) => {
	res.render('index');
});

app.get('/movies', async (req, res) => {
    let movies = await movieCollection.find().toArray()
    res.render('movies', {movies})
})

app.listen(5000, () => console.log('Server listening to port 5000...'));
