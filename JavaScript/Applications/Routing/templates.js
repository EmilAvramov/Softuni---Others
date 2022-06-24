/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html, render } from '../node_modules/lit-html/lit-html.js';
import { until } from '../node_modules/lit-html/directives/until.js';

// Guest templates

export const guest = () => html`<h1><a href="/">Furniture Store</a></h1>
	<nav>
		<div id="guest">
			<a id="loginLink" href="login.html">Login</a>
			<a id="registerLink" href="register.html">Register</a>
		</div>
	</nav>`;

export const login = () => html`<div class="container">
	<div class="row space-top">
		<div class="col-md-12">
			<h1>Login User</h1>
			<p>Please fill all fields.</p>
		</div>
	</div>
	<form>
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

// User templates

export const user = () => html`<h1><a href="/">Furniture Store</a></h1>
	<nav>
		<a id="catalogLink" href="index.html">Dashboard</a>
		<div id="user">
			<a id="createLink" href="/create">Create Furniture</a>
			<a id="profileLink" href="/home">My Publications</a>
			<a id="logoutBtn" href="/">Logout</a>
		</div>
	</nav>`;

export const details = (obj) => html`
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
						<img src=${obj.img} />
					</div>
				</div>
			</div>
			<div class="col-md-4">
				<p>Make: <span>${obj.make}</span></p>
				<p>Model: <span>${obj.model}</span></p>
				<p>Year: <span>${obj.year}</span></p>
				<p>Description: <span>${obj.description}</span></p>
				<p>Price: <span>${obj.price}</span></p>
				<p>Material: <span>${obj.material}</span></p>
				<div>
					<a href="”#”" class="btn btn-info">Edit</a>
					<a href="”#”" class="btn btn-red">Delete</a>
				</div>
			</div>
		</div>
	</div>
`;

export const dashboard = (data) => html`
	<div class="container">
		<div class="row space-top">
			<div class="col-md-12">
				<h1>Welcome to Furniture System</h1>
				<p>Select furniture from the catalog to view details.</p>
			</div>
		</div>
		${data.then((res) =>
			res.map(
				(x) => html`
					<div class="row space-top">
						<div class="col-md-4">
							<div class="card text-white bg-primary">
								<div class="card-body">
									<img src=${x.img} />
									<p>Description here</p>
									<footer>
										<p>Price: <span>${x.price}</span></p>
									</footer>
									<div>
										<a href="”#”" class="btn btn-info"
											>Details</a
										>
									</div>
								</div>
							</div>
						</div>
					</div>
				`
			)
		)}
	</div>
`;

export const createNew = () => html`
	<div class="container">
		<div class="row space-top">
			<div class="col-md-12">
				<h1>Create New Furniture</h1>
				<p>Please fill all fields.</p>
			</div>
		</div>
		<form>
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
