/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';

const navTemplateGuest = () => html`
	<header id="titlebar" class="layout">
		<a href="#" class="site-logo">Team Manager</a>
		<nav>
			<a href="#" class="action">Browse Teams</a>
			<a href="#" class="action">Login</a>
			<a href="#" class="action">Register</a>
		</nav>
	</header>
`;

const navTemplateUser = () => html`
	<header id="titlebar" class="layout">
		<a href="#" class="site-logo">Team Manager</a>
		<nav>
			<a href="#" class="action">Browse Teams</a>
			<a href="#" class="action">My Teams</a>
			<a href="#" class="action">Logout</a>
		</nav>
	</header>
`;

export function guestNav(ctx) {
	ctx.render(navTemplateGuest());
}

export function userNav(ctx) {
	ctx.render(navTemplateUser());
}
