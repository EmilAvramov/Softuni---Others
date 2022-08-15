const homeController = require('./../controllers/homeController');
const aboutController = require('./../controllers/aboutController');
const createController = require('./../controllers/createController');
const detailsController = require('./../controllers/detailsController');
const authController = require('./../controllers/authController')
const notFoundController = require('./../controllers/notFoundController');
const { isAuth } = require('../middleware/authMiddleware')

const router = require('express').Router();

router.get('/', homeController.view);
router.get('/about', aboutController.view);

router.get('/register', authController.registerView)
router.post('/register', authController.registerPost)
router.get('/login', authController.loginView)
router.post('/login', authController.loginPost)
router.get('/details/:id', detailsController.view);

router.use(isAuth)

router.get('/logout', authController.logout)

router.get('/create/cube', createController.viewCube);
router.get('/create/accessory', createController.viewAccessory)
router.post('/create/cube', createController.createCube);
router.post('/create/accessory', createController.createAccessory)

router.get('/cube/:id/attach', detailsController.attachView)
router.post('/cube/:id/attach', detailsController.attachPost)
router.get('/cube/:id/edit', detailsController.editView)
router.post('/cube/:id/edit', detailsController.editPost)

router.get('*', notFoundController.view);

module.exports = router;
