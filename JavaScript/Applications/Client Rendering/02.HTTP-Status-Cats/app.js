/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html, render } from '../node_modules/lit-html/lit-html.js';
import cats from './catSeeder.js';

const root = document.getElementById('allCats');
const template = (data) => html` <ul>
	${data.map(
		(cat) => html` <li>
			<img
				src="./images/${cat.imageLocation}.jpg"
				width="250"
				height="250"
				alt="Card image cap"
			/>
			<div class="info">
				<button class="showBtn">${cat.statusMessage}</button>
				<div class="status" style="display: none" id=${cat.id}>
					<h4>Status Code: ${cat.statusCode}</h4>
					<p>Continue</p>
				</div>
			</div>
		</li>`
	)}
</ul>`;

render(template(cats), root);
