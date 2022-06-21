const url = 'http://localhost:3030/jsonstore/collections/books';
const form = document.getElementById('form');
const loadBooks = document.getElementById('loadBooks');
const titleInput = document.getElementById('title');
const authorInput = document.getElementById('author');
const submitBtn = document.getElementById('submit');

async function getData() {
	const request = await fetch(url);
	return request.json();
}

async function getSubSet(id) {
	const request = await fetch(`${url}/${id}`);
	return request.json();
}

async function postData(obj) {
	const request = await fetch(url, {
		method: 'PATCH',
		body: JSON.stringify(obj),
	});
	return request.json();
}

async function editData(id, obj) {
	const request = await fetch(`${url}/${id}`, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request.json();
}

async function deleteItem(id) {
	const request = await fetch(`${url}/${id}`, {
		method: 'DELETE',
	});
	return request.json();
}

function clearElements() {
	titleInput.value = '';
	authorInput.value = '';
}

function createBtn(key, obj) {
	const btnNew = document.createElement('button');
	btnNew.textContent = 'Save';
	submitBtn.style.display = 'none';
	btnNew.style.display = 'block';
	btnNew.addEventListener('click', () => {
		editData(key, obj);
		form.children[0].textContent = 'Form';
		clearElements();
		submitBtn.style.display = 'block';
		btnNew.style.display = 'none';
		form.removeChild(form.lastChild);
	});
	form.appendChild(submitBtn);
}

loadBooks.addEventListener('click', () => {
	const table = document.getElementById('output');
	getData().then((obj) => {
		table.innerHTML = '';
		Object.entries(obj).forEach(([key, { author, title }]) => {
			const tr = document.createElement('tr');
			const td1 = document.createElement('td');
			td1.textContent = title;
			tr.appendChild(td1);
			const td2 = document.createElement('td');
			td2.textContent = author;
			tr.appendChild(td2);
			const btn1 = document.createElement('button');
			btn1.textContent = 'Edit';
			btn1.addEventListener('click', () => {
				getSubSet(key).then((res) => {
					form.children[0].textContent = 'Edit Form';
					titleInput.value = res.title;
					authorInput.value = res.author;
					const edited = { author: res.author, title: res.title };
					createBtn(key, edited);
				});
			});
			tr.appendChild(btn1);
			const btn2 = document.createElement('button');
			btn2.textContent = 'Delete';
			btn2.addEventListener('click', () => {
				deleteItem(key);
			});
			tr.appendChild(btn2);
			table.appendChild(tr);
		});
	});
});

form.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const author = data.get('author');
	const title = data.get('title');
	if (form.textContent === 'Form') {
		if (titleInput.value && authorInput.value) {
			const request = {
				author,
				title,
			};
			postData(request);
		} else {
			// eslint-disable-next-line no-alert
			window.alert('Please provide valid input');
		}
		clearElements();
	}
});

form.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const author = data.get('author');
	const title = data.get('title');
	if (titleInput.value && authorInput.value) {
		const request = {
			author,
			title,
		};
		postData(request);
	} else {
		// eslint-disable-next-line no-alert
		window.alert('Please provide valid input');
	}
	clearElements();
});
