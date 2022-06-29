/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';

const footerTemplate = () => html`
	<footer id="footer">SoftUni &copy; 2014-2021</footer>
`;

export function footer(ctx) {
	ctx.render(footerTemplate());
}
