const url = 'http://localhost:3030/jsonstore/collections/myboard/posts';

export async function createPost(obj) {
	const request = await fetch(url, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request.json();
}

export async function viewPosts() {
	const request = await fetch(url);
	return request.json();
}

export function reportData(e) {
	const data = new FormData(e.currentTarget);
	const datetime = new Date().toLocaleString();
	const topicName = data.get('topicName');
	const username = data.get('username');
	const postText = data.get('postText');
	const request = { topicName, username, postText, datetime };
	return request;
}
