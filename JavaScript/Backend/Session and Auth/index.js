const express = require('express');
const cookieParser = require('cookie-parser');

const app = express();

app.use(cookieParser());

app.get('/', (req, res) => {
    res.cookie('test', 'hello test')
    res.cookie('test2', 'hello test2')
	res.send('Hello World');
});

app.get('/cats', (req, res) => {
    console.log(req.cookies)
	res.send('I love cats');
});

app.listen(5000, () => console.log('Server listening in port 5000...'));