/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { render } from '../node_modules/lit-html/lit-html.js';
import * as template from './templates.js';
import * as request from './requests.js';

const head = document.querySelector('header');
const main = document.querySelector('main');

// Content
// Headers

const guestSection = () => {
	render(template.guest(), head);
};

const userSection = () => {
	render(template.user(), head);
};

// Content
// Body content

const dashboard = () => {
	render(template.dashboard(request.getAll()), main);
};

const login = () => {
	render(template.login(), main);
};

const register = () => {
	render(template.register(), main);
};

const details = (ctx) => {
	render(
		template.details(request.getSingle(ctx.page.current.split('/')[2])),
		main
	);
};

const create = () => {
	render(template.createNew(), main);
};

const edit = (ctx) => {
	render(
		template.edit(request.getSingle(ctx.page.current.split('/')[2])),
		main
	);
};

// Views
// Guests

export const guestView = () => {
	guestSection();
	dashboard();
};

export const loginView = () => {
	guestSection();
	login();
};

export const regReview = () => {
	guestSection();
	register();
};

// Views
// Users

export const dashboardView = () => {
	userSection();
	dashboard();
};

export const detailsView = (ctx) => {
	userSection();
	details(ctx);
};

export const createView = () => {
	userSection();
	create();
};

export const editView = (ctx) => {
	userSection();
	edit(ctx);
};

export const deleteView = () => {
	userSection();
	dashboard();
};
