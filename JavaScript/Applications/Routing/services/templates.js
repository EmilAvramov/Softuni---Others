/* eslint-disable no-underscore-dangle */
/* eslint-disable no-return-assign */
/* eslint-disable no-param-reassign */
/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';
import { until } from '../node_modules/lit-html/directives/until.js';
import page from '../node_modules/page/page.mjs';
import * as request from './requests.js';

// Click Events
// Login Form
const loginUser = (e) => {
	e.preventDefault();
	const formData = new FormData(e.currentTarget);
	const email = formData.get('email');
	const password = formData.get('password');
	const req = request.login({ email, password });
	req.then((data) => {
		if (data.email !== undefined) {
			localStorage.setItem('email', data.email);
			localStorage.setItem('username', data.username);
			localStorage.setItem('token', data.accessToken);
			page.redirect('/dashboard');
		}
	});
	const eml = document.getElementById('email');
	const pw = document.getElementById('password');
	eml.value = '';
	pw.value = '';
};

// Register User
const registerUser = (e) => {
	e.preventDefault();
	const formData = new FormData(e.currentTarget);
	const email = formData.get('email');
	const password = formData.get('password');
	const pw = document.getElementById('password');
	const pwRe = document.getElementById('rePass');
	if (pw.value === pwRe.value) {
		const req = request.register({ email, password });
		req.then((data) => {
			localStorage.setItem('email', data.email);
			localStorage.setItem('username', data.username);
			localStorage.setItem('token', data.accessToken);
			page.redirect('/dashboard');
		});
	} else {
		// eslint-disable-next-line no-alert
		alert('Passwords do not match');
		pw.value = '';
		pwRe.value = '';
	}
};

// Submit new item
const createData = (e) => {
	e.preventDefault();
	const formData = new FormData(e.currentTarget);
	const make = formData.get('make');
	const model = formData.get('model');
	const year = formData.get('year');
	const description = formData.get('description');
	const price = formData.get('price');
	const img = formData.get('img');
	const material = formData.get('material');

	const data = { make, model, year, description, price, img, material };
	request.create(data, localStorage.token);
	const inputs = document.querySelectorAll('input');
	inputs.forEach((el) => (el.value = ''));
	page.redirect('/dashboard');
};

// Edit existing data
const editData = (e, id) => {
	e.preventDefault();
	const formData = new FormData(e.currentTarget);
	const make = formData.get('make');
	const model = formData.get('model');
	const year = formData.get('year');
	const description = formData.get('description');
	const price = formData.get('price');
	const img = formData.get('img');
	const material = formData.get('material');

	const data = { make, model, year, description, price, img, material };
	request.update(id, data, localStorage.token);
	page.redirect('/dashboard');
};

// Logout function
const logOut = () => {
	localStorage.clear();
	page.redirect('/');
};

// Delete function
const delItem = (id, token) => {
	request.del(id, token);
	page.redirect('/dashboard');
};

// Guest templates
// Guest navigation
export const guest = () => html`<h1><a href="/">Furniture Store</a></h1>
	<nav>
		<div id="guest">
			<a id="loginLink" href="/login">Login</a>
			<a id="registerLink" href="/register">Register</a>
		</div>
	</nav>`;

// Login screen
export const login = () => html`<div class="container">
	<div class="row space-top">
		<div class="col-md-12">
			<h1>Login User</h1>
			<p>Please fill all fields.</p>
		</div>
	</div>
	<form @submit=${(e) => loginUser(e)}>
		<div class="row space-top">
			<div class="col-md-4">
				<div class="form-group">
					<label class="form-control-label" for="email">Email</label>
					<input
						class="form-control"
						id="email"
						type="text"
						name="email"
					/>
				</div>
				<div class="form-group">
					<label class="form-control-label" for="password"
						>Password</label
					>
					<input
						class="form-control"
						id="password"
						type="password"
						name="password"
					/>
				</div>
				<input type="submit" class="btn btn-primary" value="Login" />
			</div>
		</div>
	</form>
</div>`;

// Register screen
export const register = () => html`
	<div class="container">
		<div class="row space-top">
			<div class="col-md-12">
				<h1>Register New User</h1>
				<p>Please fill all fields.</p>
			</div>
		</div>
		<form @submit=${(e) => registerUser(e)}>
			<div class="row space-top">
				<div class="col-md-4">
					<div class="form-group">
						<label class="form-control-label" for="email"
							>Email</label
						>
						<input
							class="form-control"
							id="email"
							type="text"
							name="email"
						/>
					</div>
					<div class="form-group">
						<label class="form-control-label" for="password"
							>Password</label
						>
						<input
							class="form-control"
							id="password"
							type="password"
							name="password"
						/>
					</div>
					<div class="form-group">
						<label class="form-control-label" for="rePass"
							>Repeat</label
						>
						<input
							class="form-control"
							id="rePass"
							type="password"
							name="rePass"
						/>
					</div>
					<input
						type="submit"
						class="btn btn-primary"
						value="Register"
					/>
				</div>
			</div>
		</form>
	</div>
`;

// User templates
// User navigation
export const user = () => html`<h1><a href="/">Furniture Store</a></h1>
	<nav>
		<a id="catalogLink" href="/dashboard">Dashboard</a>
		<div id="user">
			<a id="createLink" href="/create">Create Furniture</a>
			<a id="profileLink" href="/">My Publications</a>
			<a @click=${logOut} id="logoutBtn" href="/">Logout</a>
		</div>
	</nav>`;

// Render function for each item
const renderItems = (obj) =>
	html` ${until(
		obj.then((res) =>
			Object.values(res).map(
				(x) => html` <div class="row space-top">
					<div class="col-md-4">
						<div class="card text-white bg-primary">
							<div class="card-body">
								<img src=${x.img} />
								<p>Description here</p>
								<footer>
									<p>Price: <span>${x.price}</span></p>
								</footer>
								<div>
									<a
										href="/details/${x._id}"
										class="btn btn-info"
										>Details</a
									>
								</div>
							</div>
						</div>
					</div>
				</div>`
			)
		)
	)}`;

// Dashboard screen
export const dashboard = (data) =>
	html`
		<div class="container">
			<div class="row space-top">
				<div class="col-md-12">
					<h1>Welcome to Furniture System</h1>
					<p>Select furniture from the catalog to view details.</p>
				</div>
			</div>
			${renderItems(data)}
		</div>
	`;

// Create item screen
export const createNew = () => html`
	<div class="container">
		<div class="row space-top">
			<div class="col-md-12">
				<h1>Create New Furniture</h1>
				<p>Please fill all fields.</p>
			</div>
		</div>
		<form @submit=${(e) => createData(e)}>
			<div class="row space-top">
				<div class="col-md-4">
					<div class="form-group">
						<label class="form-control-label" for="new-make"
							>Make</label
						>
						<input
							class="form-control valid"
							id="new-make"
							type="text"
							name="make"
						/>
					</div>
					<div class="form-group has-success">
						<label class="form-control-label" for="new-model"
							>Model</label
						>
						<input
							class="form-control is-valid"
							id="new-model"
							type="text"
							name="model"
						/>
					</div>
					<div class="form-group has-danger">
						<label class="form-control-label" for="new-year"
							>Year</label
						>
						<input
							class="form-control is-invalid"
							id="new-year"
							type="number"
							name="year"
						/>
					</div>
					<div class="form-group">
						<label class="form-control-label" for="new-description"
							>Description</label
						>
						<input
							class="form-control"
							id="new-description"
							type="text"
							name="description"
						/>
					</div>
				</div>
				<div class="col-md-4">
					<div class="form-group">
						<label class="form-control-label" for="new-price"
							>Price</label
						>
						<input
							class="form-control"
							id="new-price"
							type="number"
							name="price"
						/>
					</div>
					<div class="form-group">
						<label class="form-control-label" for="new-image"
							>Image</label
						>
						<input
							class="form-control"
							id="new-image"
							type="text"
							name="img"
						/>
					</div>
					<div class="form-group">
						<label class="form-control-label" for="new-material"
							>Material (optional)</label
						>
						<input
							class="form-control"
							id="new-material"
							type="text"
							name="material"
						/>
					</div>
					<input
						type="submit"
						class="btn btn-primary"
						value="Create"
					/>
				</div>
			</div>
		</form>
	</div>
`;

// Individual item details screen
export const details = (obj) =>
	until(
		obj.then(
			(data) => html`
				<div class="container">
					<div class="row space-top">
						<div class="col-md-12">
							<h1>Furniture Details</h1>
						</div>
					</div>
					<div class="row space-top">
						<div class="col-md-4">
							<div class="card text-white bg-primary">
								<div class="card-body">
									<img src=".${data.img}" />
								</div>
							</div>
						</div>
						<div class="col-md-4">
							<p>Make: <span>${data.make}</span></p>
							<p>Model: <span>${data.model}</span></p>
							<p>Year: <span>${data.year}</span></p>
							<p>Description: <span>${data.description}</span></p>
							<p>Price: <span>${data.price}</span></p>
							<p>Material: <span>${data.material}</span></p>
							<div>
								<a href="/edit/${data._id}" class="btn btn-info"
									>Edit</a
								>
								<a
									@click=${() =>
										delItem(data._id, localStorage.token)}
									href="/delete"
									class="btn btn-red"
									>Delete</a
								>
							</div>
						</div>
					</div>
				</div>
			`
		)
	);

// Edit screen
export const edit = (obj) =>
	until(
		obj.then(
			(data) =>
				html`
					<div class="container">
						<div class="row space-top">
							<div class="col-md-12">
								<h1>Edit Furniture</h1>
								<p>Please fill all fields.</p>
							</div>
						</div>
						<form @submit=${(e) => editData(e, data._id)}>
							<div class="row space-top">
								<div class="col-md-4">
									<div class="form-group">
										<label
											class="form-control-label"
											for="new-make"
											>Make</label
										>
										<input
											class="form-control"
											id="new-make"
											type="text"
											name="make"
											value=${data.make}
										/>
									</div>
									<div class="form-group has-success">
										<label
											class="form-control-label"
											for="new-model"
											>Model</label
										>
										<input
											class="form-control is-valid"
											id="new-model"
											type="text"
											name="model"
											value=${data.model}
										/>
									</div>
									<div class="form-group has-danger">
										<label
											class="form-control-label"
											for="new-year"
											>Year</label
										>
										<input
											class="form-control is-invalid"
											id="new-year"
											type="number"
											name="year"
											value=${data.year}
										/>
									</div>
									<div class="form-group">
										<label
											class="form-control-label"
											for="new-description"
											>Description</label
										>
										<input
											class="form-control"
											id="new-description"
											type="text"
											name="description"
											value=${data.description}
										/>
									</div>
								</div>
								<div class="col-md-4">
									<div class="form-group">
										<label
											class="form-control-label"
											for="new-price"
											>Price</label
										>
										<input
											class="form-control"
											id="new-price"
											type="number"
											name="price"
											value=${data.price}
										/>
									</div>
									<div class="form-group">
										<label
											class="form-control-label"
											for="new-image"
											>Image</label
										>
										<input
											class="form-control"
											id="new-image"
											type="text"
											name="img"
											value=${data.img}
										/>
									</div>
									<div class="form-group">
										<label
											class="form-control-label"
											for="new-material"
											>Material (optional)</label
										>
										<input
											class="form-control"
											id="new-material"
											type="text"
											name="material"
											value=${data.material}
										/>
									</div>
									<input
										type="submit"
										class="btn btn-info"
										value="Edit"
									/>
								</div>
							</div>
						</form>
					</div>
				`
		)
	);
