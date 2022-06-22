const url = 'http://localhost:3030/jsonstore/collections/myboard/comments';

export async function viewComments() {
	const request = await fetch(url);
	return request.json();
}

export async function viewPost(id) {
	const request = await fetch(`${url}/${id}`);
	return request.json();
}
