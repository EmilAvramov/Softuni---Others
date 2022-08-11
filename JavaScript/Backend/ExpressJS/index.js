const express = require('express');
const handlebars = require('express-handlebars');

const { catMiddleware } = require('./middlewares');

const app = express();
const port = 5000;

const users = [
	{
		name: 'Pesho',
		age: 20,
	},
	{
		name: 'Gosho',
		age: 30,
	},
	{
		name: 'Penka',
		age: 25,
	},
];

app.engine(
	'hbs',
	handlebars.engine({
		extname: 'hbs',
	})
);
app.set('view engine', 'hbs');
app.set('views', './ExpressJS/views');

app.use('/public', express.static('ExpressJS/public'));

app.use(catMiddleware);

app.get('/:name?', (req, res) => {
	res.render('home', { name: req.params.name || 'Guest' , users, isAuth:false});
});

app.get('/cats', (req, res) => {
	if (req.cats.length > 0) {
		res.send(req.cats.join(', '));
	} else {
		res.send('No cats to be found');
	}
});

app.get('/cats/:catId(\\d+)', (req, res) => {
	let catId = Number(req.params.catId);
	res.send(cats[catId]);
});

app.get('/express-download', (req, res) => {
	res.download('./ExpressJS/sample.pdf'); // terminate
	// res.attachment('./ExpressJS/sample.pdf') // do not terminate
});

app.get('/express-redirect', (req, res) => {
	res.redirect('/cats');
});

app.post('/cats/:catName', (req, res) => {
	req.cats.push(req.params.catName);
	res.status(201);
	res.send(`Add ${req.params.catName} to the collection`);
});

app.put('/cats', (req, res) => {
	// TODO
	res.send('Modify existing cat');
});

app.all('*', (req, res) => {
	res.status(404);
	res.send('Cannot find page');
});

app.listen(port, () => console.log(`Server listening on port ${port}...`));

// To be avoided, unnecessary
// app.get(/[0-9]/, (req, res) => {
//     res.send('This is a number page')
// })

// app.get('/cat*', (req, res) => {
//     res.send('Route with a cat?')
// })

// Vanilla JS

// const fs = require('fs');
//const path = require('path')

// app.get('/download', (req, res) => {
// 	res.writeHead(200, {
// 		// 'content-disposition': 'attachment; fileName="sample.pdf"',
//         'content-disposition': 'inline',
//         'content-type':'application/pdf'
// 	});

// 	const readStream = fs.createReadStream('./ExpressJS/sample.pdf');

//     readStream.pipe(res)

// 	// readStream.on('data', (data) => {
// 	// 	res.write(data);
// 	// });

// 	// readStream.on('end', () => res.end());
// });
// app.get('/redirect', (req, res) => {
// 	res.writeHead(302, {
// 		'location':'/cats'
// 	})
// 	res.end()
// })

// app.get('/img/:imgName', (req, res) => {
// 	res.sendFile(path.resolve('./ExpressJS/public', req.params.imgName));
// });
