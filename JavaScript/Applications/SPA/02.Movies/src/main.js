/* eslint-disable import/extensions */
import * as view from './views.js';
import { adjustNav } from './pages/nav.js';

const login = document.querySelectorAll('.nav-link')[2];
const register = document.querySelectorAll('.nav-link')[3];

adjustNav();
view.landingPage();

login.addEventListener('click', () => {
	view.loginPage();
});

register.addEventListener('click', () => {
	view.registerPage();
});
