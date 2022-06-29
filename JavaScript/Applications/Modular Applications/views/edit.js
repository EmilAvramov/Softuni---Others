/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { html } from '../node_modules/lit-html/lit-html.js';

const editTemplate = () => html`
	<main>
		<section id="edit">
			<article class="narrow">
				<header class="pad-med">
					<h1>Edit Team</h1>
				</header>
				<form id="edit-form" class="main-form pad-large">
					<div class="error">Error message.</div>
					<label>Team name: <input type="text" name="name" /></label>
					<label
						>Logo URL: <input type="text" name="logoUrl"
					/></label>
					<label
						>Description:
						<textarea name="description"></textarea>
					</label>
					<input
						class="action cta"
						type="submit"
						value="Save Changes"
					/>
				</form>
			</article>
		</section>
	</main>
`;

export function editView(ctx) {
	ctx.render(editTemplate());
}
