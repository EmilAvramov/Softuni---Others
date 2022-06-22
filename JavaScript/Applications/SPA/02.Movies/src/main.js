/* eslint-disable no-alert */
/* eslint-disable import/extensions */
import * as view from './views.js';
import * as request from './requests.js';
import { clearInputsAuth, validateAuth } from './pages/login.js';
import { clearInputsReg, validateReg } from './pages/register.js';
import { adjustNav } from './pages/nav.js';

const logout = document.querySelectorAll('.nav-link')[1];
const login = document.querySelectorAll('.nav-link')[2];
const register = document.querySelectorAll('.nav-link')[3];

const formLogin = document.querySelector('#form-login > form');
const formRegister = document.querySelector('#form-sign-up > form');
const formNewMovie = document.querySelector('#add-movie > form');

const btnAddMovie = document.getElementById('add-movie-button');

function updateView() {
	adjustNav();
	if (localStorage.token) {
		view.landingPageAuth();
	} else {
		view.landingPageGuest();
	}
}

updateView();

login.addEventListener('click', () => {
	view.loginPage();
});

register.addEventListener('click', () => {
	view.registerPage();
});

formLogin.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const email = data.get('email');
	const password = data.get('password');
	if (validateAuth()) {
		const obj = { email, password };
		request
			.authUser(obj)
			.then((user) => {
				localStorage.setItem('email', user.email);
				localStorage.setItem('password', user.password);
				localStorage.setItem('token', user.accessToken);
				updateView();
				clearInputsAuth();
			})
			.catch((err) => {
				alert(err);
				clearInputsAuth();
			});
	} else {
		alert('Please provide valid input');
	}
});

formRegister.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const email = data.get('email');
	const password = data.get('password');
	if (validateReg()) {
		const obj = { email, password };
		request
			.regUser(obj)
			.then((user) => {
				localStorage.setItem('email', user.email);
				localStorage.setItem('password', user.password);
				localStorage.setItem('token', user.accessToken);
				updateView();
				clearInputsReg();
			})
			.catch((err) => {
				alert(err);
				clearInputsReg();
			});
	} else {
		alert('Please provide valid input');
	}
});

logout.addEventListener('click', () => {
	request.logout(localStorage.accessToken);
	localStorage.clear();
	updateView();
});

btnAddMovie.addEventListener('click', () => {
	view.addMovie();
});

formNewMovie.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const title = data.get('title');
	const description = data.get('description');
	const imageUrl = data.get('imageUrl');
});
