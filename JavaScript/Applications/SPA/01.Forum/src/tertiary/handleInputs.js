const postName = document.getElementById('topicName');
const username = document.getElementById('username');
const postText = document.getElementById('postText');

export function clearInputs() {
	postName.value = '';
	username.value = '';
	postText.value = '';
}

export function checkInputs() {
	if (postName.value && username.value && postText.value) {
		return true;
	}
	return false;
}
