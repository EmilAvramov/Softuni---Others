const express = require('express');
const hbs = require('express-handlebars');
const bcrypt = require('bcrypt');
const cookieParser = require('cookie-parser');
const jwt = require('jsonwebtoken');

const userSession = {};

const app = express();
const saltRounds = 10;
const secret = 'IamAsecret';

app.use(cookieParser());
app.use('/static', express.static('public'));
app.use(express.urlencoded({ extended: false }));

app.engine(
	'hbs',
	hbs.engine({
		extname: 'hbs',
	})
);

app.set('view engine', 'hbs');

app.get('/', (req, res) => {
	let token = req.cookies['session'];

	if (token) {
		jwt.verify(token, secret, (err, decoded) => {
			if (err) {
				return res.status(401).send('Invalid token');
			}
			res.render('home', { email: decoded.email });
		});
	} else {
		res.render('home', { email: 'Guest' });
	}
});

app.get('/register', (req, res) => {
	res.render('register');
});

app.post('/register', async (req, res) => {
	const { name, email, password } = req.body;
	if (userSession[email]) {
		res.status(400).send('User already exists');
	}

	const hash = await bcrypt.hash(password, saltRounds);

	userSession[email] = {
		name,
		email,
		password: hash,
	};
	res.redirect('/login');
});

app.get('/login', (req, res) => {
	res.render('login');
});

app.post('/login', async (req, res) => {
	const { email, password } = req.body;
	const isAuth = await bcrypt.compare(password, userSession[email].password);

	if (isAuth) {
		const token = jwt.sign({email: email}, secret, {expiresIn:'1d'})
		res.cookie('session', token, {httpOnly: true});
		res.redirect('/');
	} else {
		res.status(400).send('Wrong user data');
	}
});

app.get('/logout', (req, res) => {
	res.clearCookie('session')
	res.redirect('/')
})

app.listen(5000, () => 'Server is listening to port 5000...');
