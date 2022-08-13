const homeController = require('./../controllers/indexController');
const aboutController = require('./../controllers/aboutController');
const createController = require('./../controllers/createController');
const detailsController = require('./../controllers/detailsController');
const notFoundController = require('./../controllers/notFoundController');

const router = require('express').Router();

router.get('/', homeController.view);
router.get('/about', aboutController.view);
router.get('/create', createController.view);
router.post('/create', createController.create);
router.get('/details/:id', detailsController.view);
router.get('*', notFoundController.view);

module.exports = router;
