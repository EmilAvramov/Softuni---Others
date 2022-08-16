const { urlencoded } = require('express');
const express = require('express');

const data = [
	{
		id: 1,
		name: 'first',
	},
	{
		id: 2,
		name: 'second',
	},
];

const app = express();
app.use(express.json());

app.get('/catalog', (req, res) => {
	res.json(data);
});

app.get('/catalog/:id', (req, res) => {
	const id = req.params.id;
	const item = data.find((i) => i.id == id);

	if (item) {
		res.json(item);
	} else {
		res.status(404).json({ error: 'Not found' });
	}
});

app.post('/catalog', (req, res) => {
	const item = req.body;
	item.id = Math.round(Math.random() * 9999 + 1000, 0);
	data.push(item);
	res.status(201).json(item);
});

app.put('/catalog/:id', (req, res) => {
    
	const id = req.params.id;
	const index = data.findIndex((i) => i.id == id);

    const item = req.body
    item.id = id

	if (index) {
		data.splice(index, 1, req.body);
		res.json(req.body)
	} else {
		res.status(404).json({ error: 'Not found' });
	}
});

app.delete('/catalog/:id', (req, res) => {
	const id = req.params.id;
	const index = data.findIndex((i) => i.id == id);

    const item = req.body
    item.id = id

	if (index != -1) {
		data.splice(index, 1);
		res.json(req.body)
	} else {
		res.status(404).json({ error: 'Not found' });
	}
});


app.listen(5000, () => 'Server listening on port 5000...');
