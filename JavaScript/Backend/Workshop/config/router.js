const homeController = require('../controllers/homeController');
const aboutController = require('../controllers/aboutController');
const createController = require('../controllers/createController');
const detailsController = require('../controllers/detailsController');
const authController = require('../controllers/authController');
const notFoundController = require('../controllers/notFoundController');

const router = require('express').Router();

router.use('/', homeController);
router.use('/about', aboutController);
router.use('/auth', authController);
router.use('/create', createController);
router.use('/cube', detailsController);
router.use('*', notFoundController);

module.exports = router
