/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';

const registerTemplate = () => html`
	<main>
		<section id="register">
			<article class="narrow">
				<header class="pad-med">
					<h1>Register</h1>
				</header>
				<form id="register-form" class="main-form pad-large">
					<div class="error">Error message.</div>
					<label>E-mail: <input type="text" name="email" /></label>
					<label
						>Username: <input type="text" name="username"
					/></label>
					<label
						>Password: <input type="password" name="password"
					/></label>
					<label
						>Repeat: <input type="password" name="repass"
					/></label>
					<input
						class="action cta"
						type="submit"
						value="Create Account"
					/>
				</form>
				<footer class="pad-small">
					Already have an account?
					<a href="#" class="invert">Sign in here</a>
				</footer>
			</article>
		</section>
	</main>
`;

export function registerView(ctx) {
	ctx.render(registerTemplate());
}
