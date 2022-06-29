/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';

const overlayTemplate = () => html`
	<div id="overlay" class="overlay">
		<div class="modal">
			<p>Overlay message</p>
			<a href="#" class="action">Action</a>
		</div>
	</div>
`;

export function overlay(ctx) {
	ctx.render(overlayTemplate());
}
