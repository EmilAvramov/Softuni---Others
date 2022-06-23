/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { render } from '../node_modules/lit-html/lit-html.js';
import * as request from './requests.js';
import * as template from './templates.js';

const root = document.querySelector('body');
render(template.landing(), root);

const table = document.querySelector('tbody');
const form = document.querySelector('form');
const loadData = document.getElementById('loadBooks');

render(template.addForm(), form);

form.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const title = data.get('title');
	const author = data.get('author');
	const parsed = { author, title };
	if (data.get('id')) {
		const id = data.get('id');
		request.updBook(parsed, id);
		data.set('id', '');
	} else {
		request.postBook(parsed);
	}
	render(template.withData(request.getData()), table);
	render(template.addForm(), form);
});

loadData.addEventListener('click', () => {
	render(template.withData(request.getData()), table);
	const editData = document.querySelectorAll('#edit');
	editData.forEach((btn) =>
		btn.addEventListener('click', () => {
			render(template.editForm(), form);
			const id = document.getElementById('id');
			id.value = btn.getAttribute('data-id');
		})
	);
});
