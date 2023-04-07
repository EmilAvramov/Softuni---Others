window.addEventListener('load', solve);

function solve() {
	const checkContent = (arr) => {
		return arr.filter((e) => e.value.trim() === '').length > 0;
	};

	const objectFactory = (type, text = '', elClass = '') => {
		let element = document.createElement(type);
		element.textContent = text;
		if (elClass) {
			element.classList.add(elClass);
		}
		return element;
	};

	const captureDeepCopy = (elements) => {
		let values = [];
		elements.forEach((el) => {
			values.push(el.value);
		});
		return JSON.parse(JSON.stringify(values));
	};

	let firstName = document.getElementById('first-name');
	let lastName = document.getElementById('last-name');
	let age = document.getElementById('age');
	let storyTitle = document.getElementById('story-title');
	let genre = document.getElementById('genre');
	let story = document.getElementById('story');
	let elementArray = [firstName, lastName, age, storyTitle, genre, story];

	let publishButton = document.getElementById('form-btn');
	let saveButton, editButton, deleteButton;
	let listParent = document.getElementById('preview-list');
	let form = document.querySelector('form');

	publishButton.addEventListener('click', () => {
		if (!checkContent(elementArray)) {
			elementsValues = captureDeepCopy(elementArray);
			let li = objectFactory('li', '', 'story-info');
			let htmlContent = `
						<article>
							<h4>Name: ${elementsValues[0]} ${elementsValues[1]}</h4>
							<p>Age: ${elementsValues[2]}</p>
							<p>Title: ${elementsValues[3]}</p>
							<p>Genre: ${elementsValues[4]}</p>
							<p>${elementsValues[5]}<p>
						</article>
						<button class="save-btn">Save Story</button>
						<button class="edit-btn">Edit Story</button>
						<button class="delete-btn">Delete Story</button>`;
			li.innerHTML = htmlContent;
			listParent.appendChild(li);
			form.reset();
			publishButton.disabled = true;
			saveButton = document.querySelector('.save-btn');
			editButton = document.querySelector('.edit-btn');
			deleteButton = document.querySelector('.delete-btn');

			saveButton.addEventListener('click', () => {
				let main = document.getElementById('main');
				main.innerHTML = '';
				let h1 = objectFactory('h1', 'Your scary story is saved!');
				main.appendChild(h1);
			});

			editButton.addEventListener('click', () => {
				let liElement = document.querySelector('.story-info');
				liElement.remove();
				firstName.value = elementsValues[0];
				lastName.value = elementsValues[1];
				age.value = elementsValues[2];
				storyTitle.value = elementsValues[3];
				genre.value = elementsValues[4];
				story.value = elementsValues[5];
				publishButton.disabled = false;
			});

			deleteButton.addEventListener('click', () => {
				form.reset();
				publishButton.disabled = false;
				let liElement = document.querySelector('.story-info');
				liElement.remove();
			});
		}
	});
}
