/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import page from './node_modules/page/page.mjs';
import { addLoader } from './middleware/loader.js';
import { decoratedContext } from './middleware/render.js';

page(addLoader);
page(decoratedContext);

page.start();
