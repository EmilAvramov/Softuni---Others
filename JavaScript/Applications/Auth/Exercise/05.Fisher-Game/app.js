/* To finish - 
update request to be finished
clear buttons on new catch submit
delete request to only allow deletion for owner
update and delete buttons visible to user only
*/
const urlLogin = 'http://localhost:3030/users/login';
const urlReg = 'http://localhost:3030/users/register';
const urlLogout = 'http://localhost:3030/users/logout';
const urlCatches = 'http://localhost:3030/data/catches/';
const main = document.querySelector('main');
const viewUser = document.getElementById('user');
const viewGuest = document.getElementById('guest');
const viewReg = document.getElementById('register-view');
const viewLogin = document.getElementById('login-view');
const viewHome = document.getElementById('home-view');
const btnLogin = document.getElementById('login');
const btnLogout = document.getElementById('logout');
const btnRegister = document.getElementById('register');
const btnLoad = document.querySelector('.load');
const btnAdd = document.querySelector('.add');
const welcome = document.querySelector('.email > span');
const formLogin = document.querySelector('#loginForm');
const formReg = document.querySelector('#registerForm');
const formCatch = document.getElementById('addForm');

async function getCatches() {
	const request = await fetch(urlCatches);
	return request.json();
}

async function logout(token) {
	await fetch(`${urlLogout}`, {
		method: 'GET',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
	});
}

async function doPostAuth(obj, token) {
	const request = await fetch(`${urlCatches}`, {
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
	return undefined;
}

async function authUser(obj) {
	const request = await fetch(`${urlLogin}`, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	if (request.status === 200) {
		return request.json();
	}
	return undefined;
}

async function regUser(obj) {
	const request = await fetch(`${urlReg}`, {
		method: 'POST',
		headers: { 'content-type': 'application/json' },
		body: JSON.stringify(obj),
	});
	if (request.status === 200) {
		return request.json();
	}
	return undefined;
}

async function updCatch(id, obj, token) {
	const request = await fetch(`${urlCatches}/${id}`, {
		method: 'PATCH',
		headers: {
			'content-type': 'application/json',
			'X-Authorization': token,
		},
		body: JSON.stringify(obj),
	});
	return request.json();
}

async function delCatch(id, token) {
	fetch(`${urlCatches}/${id}`, {
		method: 'DELETE',
		headers: { 'X-Authorization': token },
	});
}

function setAuthView() {
	viewGuest.style.display = 'none';
	viewUser.style.display = 'block';
	viewLogin.style.display = 'none';
	viewHome.style.display = 'block';
	viewReg.style.display = 'none';
	main.innerHTML = '';
	btnAdd.disabled = false;
	welcome.textContent = localStorage.getItem('username');
	main.appendChild(viewHome);
}

function setGuestView() {
	viewGuest.style.display = 'block';
	viewUser.style.display = 'none';
	viewLogin.style.display = 'none';
	viewHome.style.display = 'block';
	viewReg.style.display = 'none';
	main.innerHTML = '';
	btnAdd.disabled = true;
	welcome.textContent = 'guest';
	main.appendChild(viewHome);
}

function setStorage(obj) {
	localStorage.setItem('email', obj.email);
	localStorage.setItem('password', obj.password);
	localStorage.setItem('username', obj.username);
	localStorage.setItem('token', obj.accessToken);
	welcome.textContent = obj.username;
}

function createE(
	tag,
	cls,
	type = '',
	value = '',
	dataId = '',
	textC = '',
	func = ''
) {
	const el = document.createElement(tag);
	el.type = type;
	el.classList.add(cls);
	el.value = value;
	el.setAttribute('data-id', dataId);
	el.textContent = textC;
	el.addEventListener('click', () => {
		func(dataId, localStorage.getItem('token'));
	});
	return el;
}

function createL(content) {
	const label = document.createElement('label');
	label.textContent = content;
	return label;
}

function createHTML() {
	const mainE = document.getElementById('catches');
	getCatches().then((data) => {
		Object.values(data).forEach((e) => {
			const parent = document.createElement('div');
			parent.classList.add('catch');

			parent.appendChild(createL('Angler'));
			parent.appendChild(createE('input', 'angler', 'text', e.angler));
			parent.appendChild(createL('Weight'));
			parent.appendChild(createE('input', 'weight', 'text', e.weight));
			parent.appendChild(createL('Species'));
			parent.appendChild(createE('input', 'species', 'text', e.species));
			parent.appendChild(createL('Location'));
			parent.appendChild(
				createE('input', 'location', 'text', e.location)
			);
			parent.appendChild(createL('Bait'));
			parent.appendChild(createE('input', 'bait', 'text', e.bait));
			parent.appendChild(createL('Capture Time'));
			parent.appendChild(
				createE('input', 'captureTime', 'text', e.captureTime)
			);
			parent.appendChild(
				// eslint-disable-next-line no-underscore-dangle
				createE('button', 'update', '', '', e._id, 'Update')
			);
			parent.appendChild(
				// eslint-disable-next-line no-underscore-dangle
				createE('button', 'delete', '', '', e._id, 'Delete', delCatch)
			);
			mainE.appendChild(parent);
		});
	});
}

btnLoad.addEventListener('click', () => {
	createHTML();
});

btnLogin.addEventListener('click', () => {
	main.innerHTML = '';
	main.appendChild(viewLogin);
	viewLogin.style.display = 'inline-block';
	formLogin.addEventListener('submit', (event) => {
		event.preventDefault();
		const data = new FormData(event.currentTarget);
		const email = data.get('email');
		const password = data.get('password');
		const validEmail = document.getElementById('loginEmail');
		const validPw = document.getElementById('pwEmail');
		if (validEmail.value && validPw.value) {
			const request = { email, password };
			authUser(request)
				.then((res) => {
					setStorage(res);
					validEmail.value = '';
					validPw.value = '';
					setAuthView();
				})
				.catch(() => {
					// eslint-disable-next-line no-alert
					window.alert('Wrong username or password');
				});
		} else {
			// eslint-disable-next-line no-alert
			window.alert('Wrong username or password');
		}
	});
});

btnLogout.addEventListener('click', () => {
	logout(localStorage.getItem('token'));
	localStorage.clear();
	setGuestView();
});

btnRegister.addEventListener('click', () => {
	main.innerHTML = '';
	viewReg.style.display = 'inline-block';
	main.appendChild(viewReg);
	formReg.addEventListener('submit', (e) => {
		e.preventDefault();
		const data = new FormData(e.currentTarget);
		const email = data.get('email');
		const password = data.get('password');
		const validEmail = document.getElementById('regEmail');
		const validPw1 = document.getElementById('regPw1');
		const validPw2 = document.getElementById('regPw2');
		if (
			validPw1.value === validPw2.value &&
			validEmail.value &&
			validPw1.value &&
			validPw2.value
		) {
			const request = { email, password };
			regUser(request)
				.then((res) => {
					setStorage(res);
					validEmail.value = '';
					validPw1.value = '';
					validPw2.value = '';
					setAuthView();
				})
				.catch((err) => {
					// eslint-disable-next-line no-alert
					window.alert(err);
				});
		} else {
			// eslint-disable-next-line no-alert
			window.alert('Wrong username or password');
		}
	});
});

formCatch.addEventListener('submit', (e) => {
	e.preventDefault();
	const data = new FormData(e.currentTarget);
	const angler = data.get('angler');
	const weight = data.get('weight');
	const species = data.get('species');
	const location = data.get('location');
	const bait = data.get('bait');
	const captureTime = data.get('captureTime');
	const request = {
		angler,
		weight,
		species,
		location,
		bait,
		captureTime,
	};
	doPostAuth(request, localStorage.getItem('token'));
});

window.addEventListener('load', async () => {
	if (localStorage.email) {
		setAuthView();
	} else {
		setGuestView();
	}
});
