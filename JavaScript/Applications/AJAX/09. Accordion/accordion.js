const parent = document.getElementById('main');

async function getData() {
	const request = await fetch(
		'http://localhost:3030/jsonstore/advanced/articles/list'
	);
	return request.json();
}

async function getItem(id) {
	const request = await fetch(
		`http://localhost:3030/jsonstore/advanced/articles/details/${id}`
	);
	return request.json();
}

function createElement(e) {
	return document.createElement(e);
}

function addEvent(e) {
	e.addEventListener('click', () => {
		const subParent = e.parentNode;
		const child = subParent.parentNode.children[1];
		if (child.classList.contains('extra')) {
			child.classList.remove('extra');
			child.style.display = 'inline-block';
			e.textContent = 'Less';
		} else {
			child.classList.add('extra');
			child.style.display = '';
			e.textContent = 'More';
		}
	});
}

function createCards(response) {
	response.then((parsed) => {
		Object.values(parsed).forEach((property) => {
			// eslint-disable-next-line no-underscore-dangle
			getItem(property._id).then((data) => {
				const mainDiv = createElement('div');
				mainDiv.classList.add('accordion');

				const subDiv = createElement('div');
				subDiv.classList.add('head');

				const span = createElement('span');
				span.textContent = data.title;
				subDiv.appendChild(span);

				const btn = createElement('btn');
				btn.classList.add('button');
				// eslint-disable-next-line no-underscore-dangle
				btn.setAttribute('id', `${data._id}`);
				btn.textContent = 'More';
				addEvent(btn);
				subDiv.appendChild(btn);

				const lastDiv = createElement('div');
				lastDiv.classList.add('extra');

				const p = createElement('p');
				p.textContent = data.content;
				lastDiv.appendChild(p);

				mainDiv.appendChild(subDiv);
				mainDiv.appendChild(lastDiv);
				parent.appendChild(mainDiv);
			});
		});
	});
}

createCards(getData());
