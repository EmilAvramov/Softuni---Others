/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html, render } from '../node_modules/lit-html/lit-html.js';

const inputs = document.getElementById('towns');
const form = document.querySelector('form');
const root = document.getElementById('root');
const template = (data) => html` <ul>
	${data.split(', ').map((e) => html`<li>${e}</li>`)}
</ul>`;

form.addEventListener('submit', (e) => {
	e.preventDefault();
	render(template(inputs.value), root);
});
