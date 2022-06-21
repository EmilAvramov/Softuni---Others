const form = document.querySelector('form');
form.addEventListener('submit', (ev) => {
	ev.preventDefault();
	const formData = new FormData(ev.currentTarget);
	const email = formData.get('email');
	const password = formData.get('password');
	const repass = formData.get('rePass');
	if (password === repass) {
		const data = {
			email,
			password,
		};
		fetch('http://localhost:3030/users/register', {
			method: 'POST',
			headers: { 'content-type': 'application/json' },
			body: JSON.stringify(data),
		})
			.then((res) => res.json())
			.then((user) => {
				localStorage.setItem('email', user.email);
				localStorage.setItem('password', user.password);
				localStorage.setItem('token', user.accessToken);
				if (localStorage.getItem('email')) {
					window.location.replace(
						'http://localhost:5500/JavaScript/Applications/Auth/Lab/index.html'
					);
				}
			});
	}
});
