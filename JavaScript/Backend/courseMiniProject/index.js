const http = require('http');
const fs = require('fs/promises');
const qs = require('querystring');
const cats = require('./cats.json')
const breeds = require('./breeds.json')
const catTemplate = require('./functions/catTemplate')
const breedsTemplate = require('./functions/breedsTemplate')

const server = http.createServer(async (req, res) => {
	let [pathname, queryString] = req.url.split('?');
	let params = qs.parse(queryString);

	res.writeHead(200, {
		'content-type': 'text/html',
	});

	if (pathname == '/styles/site.css') {
		let siteCSS = await fs.readFile(
			'./courseMiniProject/styles/site.css',
			'utf-8'
		);
		res.writeHead(200, {
			'content-type': 'text/css',
		});
		res.write(siteCSS);
	} else if (pathname == '/api/requests.js') {
		let requests = await fs.readFile('./courseMiniProject/api/requests.js');
		res.writeHead(200, {
			'content-type': 'application/javascript',
		});
		res.write(requests);
	} else if (pathname == '/cats/add-cat') {
		if (req.method == 'GET') {
			let addCat = await fs.readFile(
				'./courseMiniProject/views/addCat.html',
				'utf-8'
			);
			let addCatModified = addCat.replace(
				'{{breeds}}',
				breeds.map((x) => breedsTemplate(x))
			);
			res.write(addCatModified);
		} else if (req.method == 'POST') {
			console.log('POST SUCCESSFUL')
		}
	} else if (pathname == '/cats/add-breed') {
		if (req.method == 'GET') {
			let addBreed = await fs.readFile(
				'./courseMiniProject/views/addBreed.html',
				'utf-8'
			);
			res.write(addBreed);
		} else if (req.method == 'POST') {
			console.log('POST SUCCESSFUL')
		}
	} else {
		let homePage = await fs.readFile(
			'./courseMiniProject/views/home.html',
			'utf-8'
		);
		let catsFilter = cats
			.filter((x) =>
				params.name ? x.name.toLowerCase().includes(params.name) : true
			)
			.map((x) => catTemplate(x))
			.join('');

		const dynamicHomePage = homePage.replace('{{cats}}', catsFilter);
		res.write(dynamicHomePage);
	}

	res.end();
});

server.listen(5000, () => console.log('Server is listening on port 5000...'));
