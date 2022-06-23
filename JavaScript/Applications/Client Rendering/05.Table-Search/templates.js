/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';
import { until } from '../node_modules/lit-html/directives/until.js';

export const load = (data) =>
	html`${until(
		data.then((res) =>
			Object.values(res).map(
				(el) => html`<tr>
					<td>${el.firstName} ${el.lastName}</td>
					<td>${el.email}</td>
					<td>${el.course}</td>
				</tr>`
			)
		)
	)}`;

export const selected = (data, srch) =>
	html`${until(
		data.then((res) =>
			Object.values(res).map((el) => {
				if (
					el.firstName.toLowerCase().includes(srch.toLowerCase()) ||
					el.lastName.toLowerCase().includes(srch.toLowerCase()) ||
					el.email.toLowerCase().includes(srch.toLowerCase()) ||
					el.course.toLowerCase().includes(srch.toLowerCase())
				) {
					return html`<tr>
						<td class="select">${el.firstName} ${el.lastName}</td>
						<td class="select">${el.email}</td>
						<td class="select">${el.course}</td>
					</tr>`;
				}
				return html`<tr>
					<td>${el.firstName} ${el.lastName}</td>
					<td>${el.email}</td>
					<td>${el.course}</td>
				</tr>`;
			})
		)
	)}`;
