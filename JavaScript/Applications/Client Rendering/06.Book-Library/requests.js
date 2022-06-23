const url = 'http://localhost:3030/jsonstore/collections/books';

export const getData = async () => {
	const request = await fetch(url);
	return request.json();
};

export const getBook = async (id) => {
	const request = await fetch(`${url}/${id}`);
	return request.json();
};

export const postBook = async (obj) => {
	const request = await fetch(url, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request.json();
};

export const updBook = async (obj, id) => {
	const request = await fetch(`${url}/${id}`, {
		method: 'PUT',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request.json();
};

export const delBook = async (id) => {
	await fetch(`${url}/${id}`, {
		method: 'DELETE',
		headers: { 'content-type': 'application/json' },
	});
};
