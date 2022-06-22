const links = document.querySelectorAll('.nav-link');
const [welcome, logout, login, register] = links;

export function adjustNav() {
	if (localStorage.getItem('email')) {
		welcome.style.display = 'block';
		welcome.textContent = `Welcome, ${localStorage.getItem('email')}`;
		logout.style.display = 'block';
		login.style.display = 'none';
		register.style.display = 'none';
	} else {
		welcome.style.display = 'block';
		welcome.textContent = 'Welcome, guest';
		logout.style.display = 'none';
		login.style.display = 'block';
		register.style.display = 'block';
	}
}

export function x() {}
