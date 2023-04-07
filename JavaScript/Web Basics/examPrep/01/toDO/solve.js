// TODO
function attachEvents() {
	const endpoint = 'http://localhost:3030/jsonstore/tasks';
	const addButton = document.getElementById('add-button');
	const loadButton = document.getElementById('load-button');
	const list = document.getElementById('todo-list');
	const title = document.getElementById('title')

	const apiRequest = async (method, data = '') => {
		if (method === 'GET') {
			const response = await fetch(endpoint, {
				method: 'GET',
			});
			return response.json();
		} else if (method === 'POST' && data) {
			const response = await fetch(endpoint, {
				method: 'POST',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ name: data }),
			});
			return response.json();
		} else if (method === 'PATCH' && data) {
			const response = await fetch(`${endpoint}/${data.id}`, {
				method: 'PATCH',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({name: data.name})
			})
			return response.json();
		} else if (method === 'DELETE' && data) {
			const response = await fetch(`${endpoint}/${data}`, {
				method: 'DELETE',
				headers: { 'Content-Type': 'application/json' },
			})
			return response.json();
		}
		
	};

	const objectFactory = (type, text = '', elClass = '', id) => {
		let element = document.createElement(type);
		element.textContent = text;
		if (elClass) {
			element.classList.add(elClass);
		}
		if (id) {
			element.setAttribute('data-id', id)
		}
		return element;
	};

	const createElement = (data) => {
		let liElement = objectFactory('li')
		let span = objectFactory('span', data.name)
		let remove = objectFactory('button', 'Remove', '', data._id)
		let edit = objectFactory('button', 'Edit', '', data._id)
		edit.addEventListener('click', editListener)
		remove.addEventListener('click', deleteListener)
		liElement.appendChild(span)
		liElement.appendChild(remove)
		liElement.appendChild(edit)
		return liElement
	};

	const renderData = () => {
		list.innerHTML = ''
		apiRequest('GET').then((res) => {
			for (const prop in res) {
				list.appendChild(createElement(res[prop]))
			}
		});
	}

	const addListener = (e) => {
		e.preventDefault();
		apiRequest('POST', title.value).then(() => renderData())
	}

	const loadListener = (e) => {
		e.preventDefault();
		renderData()
	}

	const editListener = (e) => {
		e.preventDefault()
		let target = e.currentTarget
		let parent = e.currentTarget.parentNode
		if (e.currentTarget.textContent === 'Submit') {
			const id = target.dataset.id
			const name = parent.children[0].value
			apiRequest('PATCH', {name, id}).then(() => renderData())
		} else {
			const span = parent.children[0]
			const input = objectFactory('input')
			input.value = span.textContent
			parent.replaceChild(input, span)
			target.textContent = 'Submit'
		}
	}

	const deleteListener = (e) => {
		e.preventDefault()
		const id = e.currentTarget.dataset.id
		apiRequest('DELETE', id).then(() => renderData())
	}

	addButton.addEventListener('click', addListener);

	loadButton.addEventListener('click', loadListener);
}

attachEvents();
