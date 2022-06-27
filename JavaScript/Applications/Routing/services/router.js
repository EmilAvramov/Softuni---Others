/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import page from '../node_modules/page/page.mjs';
import * as view from './views.js';

export const routes = {
	home: ('/', view.guestView),
	login: ('/login', view.loginView),
	register: ('/register', view.regReview),
	logout: ('/logout', view.guestView),
	details: ('/details', view.detailsView),
	create: ('/create', view.createView),
	edit: ('/edit', view.editView),
};

export const start = () => page.start();
