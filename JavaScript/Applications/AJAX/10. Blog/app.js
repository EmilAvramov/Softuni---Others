async function getPosts() {
	const response = await fetch('http://localhost:3030/jsonstore/blog/posts');
	return response.json();
}

async function getComments() {
	const response = await fetch(
		'http://localhost:3030/jsonstore/blog/comments'
	);
	return response.json();
}

const btnLoad = document.getElementById('btnLoadPosts');
const btnView = document.getElementById('btnViewPost');
const select = document.getElementById('posts');
const listOutput = document.getElementById('post-comments');
const titleOutput = document.getElementById('post-title');
const bodyOutput = document.getElementById('post-body');

btnLoad.addEventListener('click', () => {
	getPosts().then((data) => {
		Object.entries(data).forEach(([key, value]) => {
			const el = document.createElement('option');
			el.value = key;
			el.innerHTML = value.title;
			select.appendChild(el);
		});
	});
});

btnView.addEventListener('click', () => {
	getPosts().then((data) => {
		Object.values(data).forEach((property) => {
			if (select.value === property.id) {
				titleOutput.textContent = property.title;
				bodyOutput.textContent = property.body;
			}
		});
	});

	getComments().then((data) => {
		listOutput.innerHTML = '';
		Object.values(data).forEach((property) => {
			const el = document.createElement('li');
			if (select.value === property.postId) {
				el.textContent = property.text;
				listOutput.appendChild(el);
			}
		});
	});
});
