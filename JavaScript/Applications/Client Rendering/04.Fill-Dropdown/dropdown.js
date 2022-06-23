/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html, render } from '../node_modules/lit-html/lit-html.js';
import { until } from '../node_modules/lit-html/directives/until.js';

const url = 'http://localhost:3030/jsonstore/advanced/dropdown';
const root = document.getElementById('menu');
const form = document.querySelector('form');
const input = document.getElementById('itemText');

async function getData() {
	const request = await fetch(url);
	return request.json();
}

async function postData(obj) {
	const request = await fetch(url, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request.json();
}

const template = (data) =>
	html`${until(
		data.then((res) =>
			Object.values(res).map(
				// eslint-disable-next-line no-underscore-dangle
				(el) => html`<option value=${el._id}>${el.text}</option>`
			)
		)
	)} `;

render(template(getData()), root);
form.addEventListener('submit', (e) => {
	e.preventDefault();

	const data = new FormData(e.currentTarget);
	const text = data.get('text');
	const request = { text };
	postData(request);
	input.value = '';

	render(template(getData()), root);
});
