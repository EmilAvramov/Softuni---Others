const express = require('express');
const session = require('express-session')

const app = express();

app.use(session({
    secret: 'cat',
    resave: false,
    saveUninitialized: true,
    cookie: {secure: false}
}))

app.get('/', (req, res) => {
    req.session.username = 'Pesho' + Math.random()
	res.send('Hello World');
});

app.get('/cats', (req, res) => {
    console.log(req.session)
	res.send('I love cats');
});

app.listen(5000, () => console.log('Server listening in port 5000...'));