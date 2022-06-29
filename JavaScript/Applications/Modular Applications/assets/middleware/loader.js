/* eslint-disable import/prefer-default-export */

const loader = document.getElementById('loader');

function show() {
	loader.style.display = '';
}

function hide() {
	loader.style.display = 'none';
}

export function addLoader(ctx, next) {
	show();
	ctx.removeLoader = hide;
	next();
}
