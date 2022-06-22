function createElement(tag, cls = '', val = '', href = '') {
	const el = document.createElement(tag);
	if (cls) {
		el.classList.add(cls);
	}
	if (val) {
		el.textContent = val;
	}
	if (href) {
		el.href = href;
	}

	return el;
}

export function createTopic(obj) {
	const divContainer = createElement('div', 'topic-container');
	const divWrapper = createElement('div', 'topic-name-wrapper');
	const divTopic = createElement('div', 'topic-name');
	const linkTopic = createElement('a', 'normal', '', '#');
	const h2Title = createElement('h2', '', `${obj.topicName}`);
	const divColumns = createElement('div', 'columns');
	const emptyDiv = createElement('div');
	const p1 = createElement('p', '', `Date: ${obj.datetime}`);
	const divNickName = createElement('div', 'nick-name');
	const p2 = createElement('p', '', `Username: ${obj.username}`);
	divNickName.appendChild(p2);
	emptyDiv.appendChild(p1);
	emptyDiv.appendChild(divNickName);
	divColumns.appendChild(emptyDiv);
	linkTopic.appendChild(h2Title);
	divTopic.appendChild(linkTopic);
	divTopic.appendChild(divColumns);
	divWrapper.appendChild(divTopic);
	divContainer.appendChild(divWrapper);
	return divContainer;
}

export function x() {
	return 1;
}
