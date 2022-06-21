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
const allViews = document.getElementById('views');
const btnLogin = document.getElementById('login');
const btnLogout = document.getElementById('logout');
const btnRegister = document.getElementById('register');
const welcome = document.querySelector('.email > span');
const formLogin = document.querySelector('#loginForm');
const formReg = document.querySelector('#registerForm');

async function getData(url) {
	const request = await fetch(url);
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
	return request.json();
}

function setAuthView() {
	viewGuest.style.display = 'none';
	viewUser.style.display = 'block';
	viewLogin.style.display = 'none';
	viewHome.style.display = 'block';
	viewReg.style.display = 'none';
	main.innerHTML = '';
	main.appendChild(viewHome);
}

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
					localStorage.setItem('email', res.email);
					localStorage.setItem('password', res.password);
					localStorage.setItem('username', res.username);
					localStorage.setItem('token', res.accessToken);
					welcome.textContent = res.username;
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
	main.innerHTML = '';
	welcome.textContent = 'guest';
	viewUser.style.display = 'none';
	viewGuest.style.display = 'block';
	welcome.textContent = localStorage.getItem('username');
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
			regUser(request).then((res) => {
				localStorage.setItem('email', res.email);
				localStorage.setItem('password', res.password);
				localStorage.setItem('username', res.username);
				localStorage.setItem('token', res.accessToken);
				welcome.textContent = res.username;
				validEmail.value = '';
				validPw1.value = '';
				validPw2.value = '';
			});
			setAuthView();
		} else {
			// eslint-disable-next-line no-alert
			window.alert('Wrong username or password');
		}
	});
});

window.addEventListener('load', async () => {
	viewUser.style.display = 'none';
	viewGuest.style.display = 'none';
	viewLogin.style.display = 'none';
	viewHome.style.display = 'none';
	viewReg.style.display = 'none';
	if (localStorage.email) {
		viewUser.style.display = 'block';
		viewHome.style.display = 'block';
		main.appendChild(viewHome);
		welcome.textContent = localStorage.getItem('username');
	} else {
		viewGuest.style.display = 'block';
	}
});
