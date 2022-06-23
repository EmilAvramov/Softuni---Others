/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { render } from '../node_modules/lit-html/lit-html.js';
import * as template from './templates.js';

const url = 'http://localhost:3030/jsonstore/advanced/table';
const root = document.querySelector('tbody');
const btn = document.getElementById('searchBtn');
const input = document.getElementById('searchField');

async function getData() {
	const request = await fetch(url);
	return request.json();
}

render(template.load(getData()), root);

btn.addEventListener('click', () => {
	render(template.selected(getData(), input.value), root);
	input.value = '';
});
