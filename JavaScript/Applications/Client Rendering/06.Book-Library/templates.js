/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';
import { until } from '../node_modules/lit-html/directives/until.js';

export const landing = () => html`
	<button id="loadBooks">LOAD ALL BOOKS</button>
	<table>
		<thead>
			<tr>
				<th>Title</th>
				<th>Author</th>
				<th>Action</th>
			</tr>
		</thead>
		<tbody></tbody>
	</table>
	<form></form>
`;

export const withData = (obj) =>
	html`${until(
		obj.then((res) =>
			Object.entries(res).map(
				([key, val]) => html`
					<tr>
						<td>${val.title}</td>
						<td>${val.author}</td>
						<td>
							<button data-id=${key} id="edit">Edit</button>
							<button id="delete">Delete</button>
						</td>
					</tr>
				`
			)
		)
	)} `;

export const addForm = () => html`
	<h3>Add book</h3>
	<label>TITLE</label>
	<input type="text" name="title" placeholder="Title..." />
	<label>AUTHOR</label>
	<input type="text" name="author" placeholder="Author..." />
	<input type="submit" value="Submit" />
`;

export const editForm = () => html`
	<input id="id" type="hidden" name="id" />
	<h3>Edit book</h3>
	<label>TITLE</label>
	<input type="text" name="title" placeholder="Title..." />
	<label>AUTHOR</label>
	<input type="text" name="author" placeholder="Author..." />
	<input type="submit" value="Save" />
`;
