const homeController = require('./../controllers/indexController')
const aboutController = require('./../controllers/aboutController')
const createController = require('./../controllers/createController')
const detailsController = require('./../controllers/detailsController')
const notFoundController = require('./../controllers/notFoundController')

const router = require('express').Router()

router.get('/', homeController.index)
router.get('/about', aboutController.about)
router.get('/create', createController.create)
router.get('/details/:id', detailsController.details)
router.get('*', notFoundController.notFound)

module.exports = router