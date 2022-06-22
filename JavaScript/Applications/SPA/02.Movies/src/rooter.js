/* eslint-disable import/extensions */
import { addMovieViewHide, addMovieViewShow } from './pages/addMovie.js';
import { dtsMovieViewHide, dtsMovieViewShow } from './pages/detailMovie.js';
import { editMovieViewHide, editMovieViewShow } from './pages/editMovie.js';
import { homeViewHide, homeViewShow } from './pages/homePage.js';
import { loginViewHide, loginViewShow } from './pages/login.js';
import { registerViewHide, registerViewShow } from './pages/register.js';
import { adjustNav } from './pages/nav.js';

const show = {
	movie: addMovieViewShow,
	details: dtsMovieViewShow,
	edit: editMovieViewShow,
	home: homeViewShow,
	login: loginViewShow,
	register: registerViewShow,
};

const hide = {
	movie: addMovieViewHide,
	details: dtsMovieViewHide,
	edit: editMovieViewHide,
	home: homeViewHide,
	login: loginViewHide,
	register: registerViewHide,
};

export function navigate(action, request) {
	adjustNav();
	if (action === 'show') {
		const renderer = show[request];
		renderer();
	} else {
		const renderer = hide[request];
		renderer();
	}
}

export function x() {}
