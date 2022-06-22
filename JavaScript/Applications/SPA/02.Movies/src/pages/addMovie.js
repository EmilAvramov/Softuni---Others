const addMovieView = document.getElementById('add-movie');
const title = document.getElementById('title');
const textArea = document.querySelector('#add-movie > form > div > textarea');
const imgUrl = document.getElementById('imageUrl');

export function addMovieViewShow() {
	addMovieView.style.display = 'block';
}

export function addMovieViewHide() {
	addMovieView.style.display = 'none';
}

export function clearInputsMovie() {
	title.value = '';
	textArea.value = '';
	imgUrl.value = '';
}

export function validateMovie() {
	if (title.value && textArea.value && imgUrl.value) {
		return true;
	}
	return false;
}
