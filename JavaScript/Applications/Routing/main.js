/* eslint-disable import/extensions */
/* eslint-disable import/no-relative-packages */
import page from './node_modules/page/page.mjs';
import * as view from './services/views.js';

page('/', view.guestView);
page('/login', view.loginView);
page('/register', view.regReview);
page('/logout', view.guestView);
page('/dashboard', view.dashboardView);
page('/details/:id', view.detailsView);
page('/create', view.createView);
page('/edit/:id', view.editView);
page('/delete', view.deleteView);

page.start();
