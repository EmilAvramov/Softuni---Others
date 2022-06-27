/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { render } from '../node_modules/lit-html/lit-html.js';
import * as template from './templates.js';
import * as request from './requests.js';

const head = document.querySelector('header');
const main = document.querySelector('main');

const guestSection = () => {
	render(template.guest(), head);
};

const userSection = () => {
	render(template.user(), head);
};

export const guestView = (obj) => {
	render(template.guest(), head);
	render(template.dashboard(request.getAll(obj)), main);
};

export const loginView = () => {
	guestSection();
	render(template.login(), main);
};

export const regReview = () => {
	guestSection();
	render(template.register(), main);
};

export const detailsView = (id) => {
	userSection();
	render(template.details(request.getSingle(id)), main);
};

export const createView = () => {
	userSection();
	render(template.createNew(), main);
};

export const editView = (id) => {
	userSection();
	render(template.edit(request.getSingle(id)), main);
};
