let button = document.querySelector('#load');
button.addEventListener('click', () => {
	let url = 'https://api.github.com/users/testnakov/repos';
	const request = new XMLHttpRequest();
	request.addEventListener('readystatechange', () => {
		if (request.readyState == 4 && request.status == 200) {
			let data = JSON.parse(request.responseText);
			document.getElementById('res').textContent = data
				.map((x) => x.name)
				.join(', ');
		}
	});
	request.open('GET', url);
	request.send();
});
