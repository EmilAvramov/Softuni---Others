const url = 'http://localhost:3030/jsonstore/phonebook';

async function getData() {
	const request = await fetch(url);
	return request.json();
}

async function postData(obj) {
	const request = await fetch(url, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	return request.json();
}

async function deleteData(key) {
	const request = await fetch(`${url}/${key}`, {
		method: 'DELETE',
	});
	return request.json();
}

const phonebook = document.getElementById('phonebook');
const btnLoad = document.getElementById('btnLoad');

btnLoad.addEventListener('click', () => {
	getData().then((data) => {
		Object.entries(data).forEach(([key, value]) => {
			const div = document.createElement('div');
			div.textContent = `${value.person} ${value.phone}`;
			const btn = document.createElement('button');
			btn.textContent = 'Delete';
			btn.addEventListener('click', () => {
				deleteData(key);
			});
			div.appendChild(btn);
			phonebook.appendChild(div);
		});
	});
});

const person = document.getElementById('person');
const phone = document.getElementById('phone');
const btnCreate = document.getElementById('btnCreate');

btnCreate.addEventListener('click', () => {
	const personData = person.value;
	const phoneData = phone.value;
	const data = {
		person: personData,
		phone: phoneData,
	};
	postData(data);
	person.value = '';
	phone.value = '';
});
