const loginView = document.getElementById('form-login');
const buttons = document.querySelectorAll('#form-login > form > div > input');

export function loginViewShow() {
	loginView.style.display = 'block';
}

export function loginViewHide() {
	loginView.style.display = 'none';
}

export function clearInputsAuth() {
	buttons[0].value = '';
	buttons[1].value = '';
}

export function validateAuth() {
	if (buttons[0].value && buttons[1].value) {
		return true;
	}
	return false;
}
