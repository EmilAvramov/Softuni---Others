const registerView = document.getElementById('form-sign-up');
const buttons = document.querySelectorAll('#form-sign-up > form > div > input');

export function registerViewShow() {
	registerView.style.display = 'block';
}

export function registerViewHide() {
	registerView.style.display = 'none';
}

export function clearInputsReg() {
	buttons[0].value = '';
	buttons[1].value = '';
	buttons[2].value = '';
}

export function validateReg() {
	if (buttons[0].value && buttons[1].value && buttons[2].value) {
		if (buttons[1].value === buttons[2].value) {
			return true;
		}
		return false;
	}
	return false;
}
