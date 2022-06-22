/* eslint-disable import/extensions */
import { viewPosts, createPost, reportData } from './requests/post.js';
import { createTopic } from './tertiary/createElement.js';
import { clearInputs, checkInputs } from './tertiary/handleInputs.js';
import { viewComments, viewPost } from './requests/comment.js';

// To finish - integrate comment requests and check architecture

const form = document.querySelector('.new-topic-border > form');
const cancel = document.getElementById('cancel');

const parentTitle = document.querySelector('.topic-title');

viewPosts().then((data) => {
	parentTitle.style.display = 'block';
	Object.values(data).forEach((el) => {
		parentTitle.appendChild(createTopic(el));
	});
});

form.addEventListener('submit', (e) => {
	e.preventDefault();
	if (checkInputs()) {
		createPost(reportData(e));
		clearInputs();
	} else {
		clearInputs();
		// eslint-disable-next-line no-alert
		alert('Please enter valid data');
	}
});

cancel.addEventListener('click', () => {
	clearInputs();
});
