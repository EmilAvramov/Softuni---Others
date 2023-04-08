// TODO:
function attachEvents() {
	const endpoint = 'http://localhost:3030/jsonstore/tasks';
	const loadButton = document.getElementById('load-board-btn');
	const createButton = document.getElementById('create-task-btn');
    const form = document.querySelector('form');

	const title = document.getElementById('title');
	const description = document.getElementById('description');

    const toDo = document.getElementById('todo-section');
    const inProgress = document.getElementById('in-progress-section')
    const codeReview = document.getElementById('code-review-section');
    const done = document.getElementById('done-section');

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
				body: JSON.stringify(data),
			});
			return response.json();
		} else if (method === 'PATCH' && data) {
			const response = await fetch(`${endpoint}/${data.id}`, {
				method: 'PATCH',
				headers: { 'Content-Type': 'application/json' },
				body: JSON.stringify({ status: data.status }),
			});
			return response.json();
		} else if (method === 'DELETE' && data) {
			const response = await fetch(`${endpoint}/${data}`, {
				method: 'DELETE',
				headers: { 'Content-Type': 'application/json' },
			});
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
			element.setAttribute('data-id', id);
		}
		return element;
	};

    const statuses = {
        'ToDo':'Move to In Progress',
        'In Progress': 'Move to Code Review',
        'Code Review': 'Move to Done',
        'Done': 'Close'
    }

	const createTask = (data) => {
		let liElement = objectFactory('li', '', 'task');
		let h3Element = objectFactory('h3', data.title);
		let pElement = objectFactory('p', data.description);
		let button = objectFactory('button', statuses[data.status], '', data._id);
        if (data.status === 'Done') {
            button.addEventListener('click', deleteTask)
        } else {
            button.addEventListener('click', moveTask)
        }
        
		liElement.appendChild(h3Element);
		liElement.appendChild(pElement);
		liElement.appendChild(button);
		return liElement;
	};

    const moveTask = (e) => {
        e.preventDefault();
        let target = e.currentTarget
		let task = target.parentNode
        let section = task.parentNode

        if (section.id === 'todo-section') {
            apiRequest('PATCH', {
                id: target.dataset.id,
                status: 'In Progress'
            }).then(() => renderData())
        } else if (section.id === 'in-progress-section') {
            apiRequest('PATCH', {
                id: target.dataset.id,
                status: 'Code Review'
            }).then(() => renderData())
        } else if (section.id === 'code-review-section') {
            apiRequest('PATCH', {
                id: target.dataset.id,
                status: 'Done'
            }).then(() => renderData())
        }
    }

    const deleteTask = (e) => {
        e.preventDefault()
        const id = e.currentTarget.dataset.id
		apiRequest('DELETE', id).then(() => renderData())
    }

    const renderData = () => {
        toDo.innerHTML = '';
        inProgress.innerHTML = '';
        codeReview.innerHTML = '';
        done.innerHTML = '';

        apiRequest('GET').then((res) => {
			for (const prop in res) {
                let element = res[prop]
                if (element.status === 'ToDo') {
                    toDo.appendChild(createTask(element))
                } else if (element.status === 'In Progress') {
                    inProgress.appendChild(createTask(element))
                } else if (element.status === 'Code Review') {
                    codeReview.appendChild(createTask(element))
                } else if (element.status === 'Done') {
                    done.appendChild(createTask(element))
                }
			}
		});
    }

    loadButton.addEventListener('click', (e) => {
        e.preventDefault()
        renderData()
    })

	createButton.addEventListener('click', (e) => {
		e.preventDefault();
		const titleData = title.value;
		const descData = description.value;
		const status = 'ToDo';
		let data = {
			title: titleData,
			description: descData,
			status: status,
		};
        form.reset()
		apiRequest('POST', data).then(() => {
            renderData()
		});
	});
}

attachEvents();
