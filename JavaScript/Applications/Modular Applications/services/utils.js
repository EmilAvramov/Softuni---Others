export function getUserData() {
	return JSON.parse(localStorage.getItem('user'));
}

export function getToken() {
	const user = getUserData();
	if (user) {
		return user.accessToken;
	}
	return null;
}

export function clearUserData() {
	localStorage.removeItem('user');
}

export function setUserData(data) {
	localStorage.setItem('user', JSON.stringify(data));
}
