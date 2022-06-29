/* eslint-disable import/prefer-default-export */
/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { render } from '../node_modules/lit-html/lit-html.js';

const root = document.getElementById('content');

function ctxRender(ctx) {
	render(ctx, root);
}

export function decoratedContext(ctx, next) {
	ctx.render = ctxRender;
	next();
}
