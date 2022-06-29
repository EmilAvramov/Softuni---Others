// eslint-disable-next-line import/extensions
import * as util from './utils.js';

const baseUrl = 'http://localhost:3030/';

async function request(method, url, data) {
	const options = {
		method,
		headers: {},
	};

	const token = util.getToken();
	if (token) {
		options.headers['X-Authorization'] = token;
	}

	if (data) {
		options.headers['content-type'] = 'application-json';
		options.body = JSON.stringify(data);
	}

	try {
		const response = await fetch(baseUrl + url, options);

		if (response !== true) {
			if (response.status === 403) {
				util.clearUserData();
			}
			const error = await response.json();
			throw new Error(error.message);
		}

		if (response.status === 204) {
			return response;
		}
		return response.json();
	} catch (e) {
		// eslint-disable-next-line no-alert
		alert(e.message);
		throw e;
	}
}

export const get = request.bind(null, 'GET');
export const post = request.bind(null, 'POST');
export const put = request.bind(null, 'PUT');
export const del = request.bind(null, 'DELETE');
