async function getData() {
	const request = await fetch(
		'http://localhost:3030/jsonstore/advanced/profiles'
	);
	return request.json();
}

function createElement(e) {
	return document.createElement(e);
}

function createHTML(obj) {
	let idx = 0;
	for (const property of obj) {
		const mainDiv = createElement('div');
		mainDiv.classList.add('profile');

		const img = createElement('img');
		img.src = 'iconProfile2.png';
		img.classList.add('userIcon');
		mainDiv.appendChild(img);

		const label1 = createElement('label');
		label1.innerHTML = 'Lock';
		mainDiv.appendChild(label1);

		const radio1 = createElement('input');
		radio1.setAttribute('type', 'radio');
		radio1.name = `user${idx}Locked`;
		radio1.value = 'lock';
		radio1.checked = true;
		mainDiv.appendChild(radio1);

		const label2 = createElement('label');
		label2.innerHTML = 'Unlock';
		mainDiv.appendChild(label2);

		const radio2 = createElement('input');
		radio2.setAttribute('type', 'radio');
		radio2.name = `user${idx}Locked`;
		radio2.value = 'unlock';
		mainDiv.appendChild(radio2);

		const br = createElement('br');
		mainDiv.appendChild(br);

		const hr = createElement('hr');
		mainDiv.appendChild(hr);

		const label3 = createElement('label');
		label3.innerHTML = 'Username';
		mainDiv.appendChild(label3);

		const input1 = createElement('input');
		input1.setAttribute('type', 'text');
		input1.name = `user${idx}UserName`;
		input1.value = property.username;
		input1.disabled = 'true';
		input1.readonly = 'true';
		mainDiv.appendChild(input1);

		const subDiv = createElement('div');
		subDiv.classList.add('user1Username');
		subDiv.setAttribute('id', `user${idx}HiddenFields`);
		subDiv.style.display = 'none';

		subDiv.appendChild(hr);

		const label4 = createElement('label');
		label4.innerHTML = 'Email:';
		subDiv.appendChild(label4);

		const input2 = createElement('input');
		input2.setAttribute('type', 'email');
		input2.name = `user${idx}Email`;
		input2.value = property.email;
		input2.disabled = 'true';
		input2.readonly = 'true';
		subDiv.appendChild(input2);

		const label5 = createElement('label');
		label5.innerHTML = 'Age:';
		subDiv.appendChild(label5);

		const input3 = createElement('input');
		input3.setAttribute('type', 'email');
		input3.name = `user${idx}Age`;
		input3.value = property.age;
		input3.disabled = 'true';
		input3.readonly = 'true';
		subDiv.appendChild(input3);

		mainDiv.appendChild(subDiv);

		const btn = createElement('button');
		btn.innerHTML = 'Show more';
		btn.addEventListener('click', () => {
			if (btn.parentNode.children[2].checked === false) {
				if (btn.parentNode.children[8].style.display === 'none') {
					btn.parentNode.children[8].style.display = 'inline-block';
					btn.parentNode.children[8].width = '100%';
				} else {
					btn.parentNode.children[8].style.display = 'none';
				}
			}
		});
		mainDiv.appendChild(btn);

		parent.appendChild(mainDiv);

		idx++;
	}
}

function createCards() {
	const data = getData().then((value) => {
		let profiles = Object.values(value);
		createHTML(profiles);
	});
	return data;
}

let parent = document.getElementById('main');
