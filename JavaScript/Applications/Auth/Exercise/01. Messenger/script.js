function postData(obj) {
	const request = fetch('http://localhost:3030/jsonstore/messenger', {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request;
}

async function refreshData() {
	const request = await fetch('http://localhost:3030/jsonstore/messenger');
	return request.json();
}

const data = document.getElementById('form');
data.addEventListener('submit', (e) => {
	e.preventDefault();
	const formInfo = new FormData(data);
	const author = formInfo.get('name');
	const content = formInfo.get('message');
	const request = {
		author,
		content,
	};
	postData(request);
});

const reset = document.getElementById('reload');
const output = document.getElementById('result');
reset.addEventListener('click', (e) => {
	e.preventDefault();
	refreshData().then((res) => {
		output.innerHTML = '';
		Object.values(res).forEach(({ author, content }) => {
			const div = document.createElement('div');
			div.textContent = `${author}: ${content}`;
			output.appendChild(div);
		});
	});
});
