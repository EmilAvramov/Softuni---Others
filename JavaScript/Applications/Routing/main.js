/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import { render } from './node_modules/lit-html/lit-html.js';
import * as template from './services/templates.js';
import * as request from './services/requests.js';

const head = document.querySelector('header');
const main = document.querySelector('main');

render(template.guest(), head);
render(template.dashboard(request.getAll()), main);
