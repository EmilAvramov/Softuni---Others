const url = 'http://localhost:3030/jsonstore/collections/students';

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

const form = document.getElementById('form');
form.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const firstName = data.get('firstName');
	const lastName = data.get('lastName');
	const facultyNumber = data.get('facultyNumber');
	const grade = data.get('grade');

	const combined = {
		firstName,
		lastName,
		facultyNumber,
		grade,
	};
	postData(combined);
	const inputs = document.querySelectorAll('input');
	inputs.forEach((el) => {
		// eslint-disable-next-line no-param-reassign
		el.value = '';
	});
});

function createHTML() {
	const table = document.getElementById('results');
	getData().then((obj) => {
		table.innerHTML = '';
		Object.values(obj).forEach(
			({ firstName, lastName, facultyNumber, grade }) => {
				const tr = document.createElement('tr');
				const td1 = document.createElement('td');
				td1.textContent = firstName;
				tr.appendChild(td1);
				const td2 = document.createElement('td');
				td2.textContent = lastName;
				tr.appendChild(td2);
				const td3 = document.createElement('td');
				td3.textContent = facultyNumber;
				tr.appendChild(td3);
				const td4 = document.createElement('td');
				td4.textContent = grade;
				tr.appendChild(td4);
				table.appendChild(tr);
			}
		);
	});
}

createHTML();
