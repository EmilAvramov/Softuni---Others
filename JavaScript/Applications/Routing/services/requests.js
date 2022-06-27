const regBaseUrl = 'http://localhost:3030/users/';
const dataBaseUrl = 'http://localhost:3030/data/catalog';
const eml = document.getElementById('email');
const pw = document.getElementById('password');

// Users

export const register = async (user) => {
	const request = await fetch(`${regBaseUrl}register`, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(user),
	});
	if (request.status !== 200) {
		// eslint-disable-next-line no-alert
		alert('Wrong details entered.');
		eml.value = '';
		pw.value = '';
	} else {
		return request.json();
	}
	return undefined;
};

export const login = async (user) => {
	const request = await fetch(`${regBaseUrl}login`, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(user),
	});
	if (request.status !== 200) {
		// eslint-disable-next-line no-alert
		alert('Wrong details entered.');
		eml.value = '';
		pw.value = '';
	} else {
		return request.json();
	}
	return undefined;
};

export const logout = async () => fetch(`${regBaseUrl}logout`);

// Data

export const create = async (data, token) => {
	const request = await fetch(dataBaseUrl, {
		method: 'POST',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
		body: JSON.stringify(data),
	});
	return request.json();
};

export const getAll = async () => {
	const request = await fetch(dataBaseUrl);
	return request.json();
};

export const getSingle = async (id) => {
	const request = await fetch(`${dataBaseUrl}/${id}`);
	return request.json();
};

export const update = async (id, data, token) => {
	const request = await fetch(`${dataBaseUrl}/${id}`, {
		method: 'PUT',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
		body: JSON.stringify(data),
	});
	return request.json();
};

export const del = async (id, token) => {
	const request = await fetch(`${dataBaseUrl}/${id}`, {
		method: 'DELETE',
		headers: {
			'X-Authorization': token,
		},
	});
	return request.json();
};

export const getOwn = async (id, ownerId) => {
	const request = await fetch(
		`${dataBaseUrl}?where=${ownerId}%3D%22${id}%22`
	);
	return request.json();
};
