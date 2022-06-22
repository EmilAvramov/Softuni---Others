/* eslint-disable import/extensions */
import { movieList, movieCard } from './factory.js';
import * as request from '../services/requests.js';

const detailsMovieView = document.getElementById('movie');
const title = document.querySelector('.text-center');
const addMovieBtn = document.getElementById('add-movie-button');

export function dtsMovieViewShow() {
	title.style.display = 'block';
	addMovieBtn.style.display = 'block';
	detailsMovieView.style.display = 'block';
}

export function dtsMovieViewHide() {
	title.style.display = 'none';
	addMovieBtn.style.display = 'none';
	detailsMovieView.style.display = 'none';
}

export function generateMovies() {
	request.getMovies().then((res) => {
		Object.values(res).forEach((movie) => {
			movieList(movie);
		});
	});
}

export function getDetails(id) {
	request.getMovie(id).then((data) => {
		movieCard(data);
	});
}
