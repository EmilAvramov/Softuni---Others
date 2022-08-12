const homeController = require('../controllers/homeController')
const movieController = require('../controllers/movieController')

const router = require('express').Router();

router.get('/', homeController.view);
router.get('/movies', movieController.view);
router.post('/create', movieController.create)

module.exports = router;