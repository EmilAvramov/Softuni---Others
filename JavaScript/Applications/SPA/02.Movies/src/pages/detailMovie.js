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
