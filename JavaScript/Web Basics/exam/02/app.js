window.addEventListener('load', solve);

function solve() {
	const checkContent = (arr) => {
		return arr.filter((e) => e.value.trim() === '').length > 0;
	};

	const captureDeepCopy = (elements) => {
		let values = [];
		elements.forEach((el) => {
			values.push(el.value);
		});
		return JSON.parse(JSON.stringify(values));
	};

    const getPicture = (value) => {
        if (value === 'Feature') {
            return '&#8865;'
        } else if (value === 'Low Priority Bug'){
            return '&#9737;'
        } else if (value === 'High Priority Bug') {
            return '&#9888;'
        }
    }

    const getClass = (value) => {
        if (value === 'Feature') {
            return 'feature'
        } else if (value === 'Low Priority Bug'){
            return 'low-priority'
        } else if (value === 'High Priority Bug') {
            return 'high-priority'
        }
    }
    let currentPoints = 0;

    const title = document.getElementById('title');
    const description = document.getElementById('description');
    const label = document.getElementById('label');
    const points = document.getElementById('points');
    const assignee = document.getElementById('assignee');

    const taskInput = document.getElementById('task-id');
    const createBtn = document.getElementById('create-task-btn');
    const deleteBtn = document.getElementById('delete-task-btn');
    const parent = document.getElementById('tasks-section')
    const form = document.getElementById('create-task-form')
    const pointsElement = document.getElementById('total-sprint-points');

    const elements = [title, description, label, points, assignee]

    createBtn.addEventListener('click', (e) => {
        if (!checkContent(elements)) {
            e.preventDefault()
            const elementsValues = captureDeepCopy(elements);
            const nextId = parent.getElementsByTagName('article').length + 1
            const html = `
                <article id="task-${nextId}" class="task-card">
                    <div class="task-card-label ${getClass(elementsValues[2])}">${elementsValues[2]} ${getPicture(elementsValues[2])}</div>
                    <h3 class="task-card-title">${elementsValues[0]}</h3>
                    <p class="task-card-description">${elementsValues[1]}</p>
                    <div class="task-card-points">Estimated at ${elementsValues[3]} pts</div>
                    <div class="task-card-assignee">Assigned to ${elementsValues[4]}</div>
                    <div class="task-card-actions">
                        <button>Delete</button>
                    </div>
                </article>
            `
            parent.innerHTML += html
            form.reset()
            const taskParent = document.getElementById(`task-${nextId}`)
            const taskDelete = taskParent.children[5].children[0]
            currentPoints += Number(elementsValues[3])
            pointsElement.textContent = `Total Points ${currentPoints}pts`
            taskDelete.addEventListener('click', (e) => {
                e.preventDefault()
                title.value = elementsValues[0];
                description.value = elementsValues[1];
                label.value = elementsValues[2];
                points.value = elementsValues[3];
                assignee.value = elementsValues[4];
                elements.forEach(element => element.disabled = true);
                createBtn.disabled = true;
                deleteBtn.disabled = false;
                taskInput.value = parent.id

                deleteBtn.addEventListener('click', (e) => {
                    e.preventDefault()
                    currentPoints -= Number(elementsValues[3])
                    pointsElement.textContent = `Total Points ${currentPoints}pts`
                    taskParent.remove()
                    form.reset()
                    createBtn.disabled = false;
                    deleteBtn.disabled = true;
                    elements.forEach(element => element.disabled = false);
                })
            })
        }
    })
}