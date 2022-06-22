/* eslint-disable import/extensions */
import { navigate } from './rooter.js';

export function landingPage() {
	navigate('show', 'home');
	navigate('hide', 'details');
	navigate('hide', 'edit');
	navigate('hide', 'login');
	navigate('hide', 'register');
	navigate('hide', 'movie');
}

export function loginPage() {
	navigate('hide', 'home');
	navigate('hide', 'details');
	navigate('hide', 'edit');
	navigate('show', 'login');
	navigate('hide', 'register');
	navigate('hide', 'movie');
}

export function registerPage() {
	navigate('hide', 'home');
	navigate('hide', 'details');
	navigate('hide', 'edit');
	navigate('hide', 'login');
	navigate('show', 'register');
	navigate('hide', 'movie');
}
