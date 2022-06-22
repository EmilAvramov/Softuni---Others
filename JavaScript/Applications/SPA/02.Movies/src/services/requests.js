const urlMovies = 'http://localhost:3030/jsonstore/data/movies';
const urlLogin = 'http://localhost:3030/users/login';
const urlReg = 'http://localhost:3030/users/register';
const urlLogout = 'http://localhost:3030/users/logout';
const urlLikes = 'http://localhost:3030/data/likes';

// Likes

export const getLikes = () => fetch(urlLikes).then((res) => res.json);
export const getMovieLikes = (id, userId) => {
	fetch(
		`${urlLikes}?where=movieId%3D%22${id}%22%20and%20_ownerId%3D%22${userId}%22`
	).then((res) => res.json());
};
export const removeLike = (id, token) =>
	fetch(`${urlLikes}/${id}`, {
		method: 'PATCH',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
	}).then((res) => res.json());

// Movie requests
export const getMovies = () => fetch(urlMovies).then((res) => res.json());
export const getMovie = (id) =>
	fetch(`${urlMovies}/${id}`).then((res) => res.json());

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
