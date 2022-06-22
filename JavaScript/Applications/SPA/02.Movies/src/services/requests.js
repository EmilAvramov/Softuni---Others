const urlMovies = 'http://localhost:3030/jsonstore/data/movies';
const urlLogin = 'http://localhost:3030/users/login';
const urlReg = 'http://localhost:3030/users/register';
const urlLogout = 'http://localhost:3030/users/logout';
const urlLikes = 'http://localhost:3030/data/likes';

// Likes

export async function getLikes() {
	const request = await fetch(urlLikes);
	return request.json();
}

export async function getMovieLikes(id, userId) {
	const request = await fetch(
		`${urlLikes}?where=movieId%3D%22${id}%22%20and%20_ownerId%3D%22${userId}%22`
	);
	return request.json();
}

export async function removeLike(id, token) {
	await fetch(`${urlLikes}/${id}`, {
		method: 'PATCH',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
	});
}

// Movie requests

export async function getMovies() {
	const request = await fetch(urlMovies);
	return request.json();
}

export async function getMovie(id) {
	const request = await fetch(`${urlMovies}/${id}`);
	return request.json();
}

export async function postMovies(obj, token) {
	const request = await fetch(urlMovies, {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
		body: JSON.stringify(obj),
	});
	if (request.status === 200) {
		return request.json();
	}
	throw Error('Wrong data');
}

export async function updMovie(obj, id, token) {
	const request = await fetch(`${urlMovies}/${id}`, {
		method: 'PATCH',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
		body: JSON.stringify(obj),
	});
	return request.json();
}

export async function delMovie(id, token) {
	await fetch(`${urlMovies}/${id}`, {
		method: 'DELETE',
		headers: { 'X-Authorization': token },
	});
}

// User requests

export async function authUser(obj) {
	const request = await fetch(urlLogin, {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
		},
		body: JSON.stringify(obj),
	});
	if (request.status === 200) {
		return request.json();
	}
	throw Error('Wrong credentials');
}

export async function regUser(obj) {
	const request = await fetch(urlReg, {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
		},
		body: JSON.stringify(obj),
	});
	if (request.status === 200) {
		return request.json();
	}
	if (request.status === 409) {
		throw Error('User already exists');
	}
	throw Error('An error occurred');
}

export async function logout(token) {
	await fetch(`${urlLogout}`, {
		method: 'GET',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
	});
}
