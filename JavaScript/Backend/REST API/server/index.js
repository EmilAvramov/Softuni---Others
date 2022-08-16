const express = require('express');

const app = express();

app.get('/data/catalog', (req, res) => {
	res.setHeader('Access-Control-Allow-Origin', '*');
	res.setHeader(
		'Access-Control-Allow-Origin',
		'GET, POST, PUT, DELETE, HEAD, OPTIONS'
	);
    res.setHeader('Access-Control-Allow-Origin', 'X-Authorization')
	res.json({});
});

app.listen(3030, () => 'Server listening to port 3030...');
