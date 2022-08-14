const express = require('express');
const cookieParser = require('cookie-parser');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

const app = express();
const saltRounds = 10;
const hashedPassword =
	'$2b$10$GZfRNnkaL6rTSMd0rXV60eSwAq9o..N.Pz0VXJWAyA0IawodLWqV6';
const secret = 'MySuperSecretSecret';

app.use(cookieParser());

app.get('/', (req, res) => {
	res.send('Hello World');
});

app.get('/hash/:password?', async (req, res) => {
	const salt = await bcrypt.genSalt(saltRounds);
	const hash = await bcrypt.hash(req.params.password, salt);

	console.log('salt: ', salt);
	console.log('hash:', hash);
	res.send('Authenticated');
});

app.get('/login/:password', async (req, res) => {
	const matched = await bcrypt.compare(req.params.password, hashedPassword);
	if (matched) {
		const payload = {
			username: 'Pesho',
		};
		const options = { expiresIn: '2d' };
		const token = jwt.sign(payload, secret, options);

		res.send(token);
	} else {
		res.send('Not Welcome');
	}
});

app.get('/verify/:token', (req, res) => {
	jwt.verify(req.params.token, secret, (err, decoded) => {
		if (err) {
			return res.status(401).send('No permissions');
		} else {
			res.json(decoded)
		}
	});
});

app.listen(5000, () => console.log('Server listening in port 5000...'));
