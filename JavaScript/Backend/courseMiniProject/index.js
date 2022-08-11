const http = require('http');
const fs = require('fs/promises');
const qs = require('querystring');
const { render } = require('./functions/renderPage');

const catTemplate = (cat) => `
        <li>
            <img
                src="${cat.imageUrl}"
                alt="Black Cat"
            />
            <h3>${cat.name}</h3>
            <p><span>Breed: </span>${cat.breed}</p>
            <p>
                <span>Description: </span>${cat.description}}
            </p>
            <ul class="buttons">
                <li class="btn edit"><a href="">Change Info</a></li>
                <li class="btn delete"><a href="">New Home</a></li>
            </ul>
        </li>`;

const server = http.createServer(async (req, res) => {
	let [pathname, queryString] = req.url.split('?');
	let params = qs.parse(queryString);

	res.writeHead(200, {
		'content-type': 'text/html',
	});

	if (req.url == '/styles/site.css') {
		let siteCSS = await fs.readFile(
			'./courseMiniProject/styles/site.css',
			'utf-8'
		);
		res.writeHead(200, {
			'content-type': 'text/css',
		});
		res.write(siteCSS);
	} else if (req.url == '/cats/add-cat') {
		await render(res, './courseMiniProject/views/addCat.html');
	} else if (req.url == '/cats/add-breed') {
		await render(res, './courseMiniProject/views/addBreed.html');
	} else {
		let homePage = await fs.readFile(
			'./courseMiniProject/views/home.html',
			'utf-8'
		);
		let catsRes = await fs.readFile('./courseMiniProject/cats.json');
		let catsFilter = JSON.parse(catsRes)
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
