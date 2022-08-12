const cubeService = require('../services/cubeService')

exports.view = (req, res) => {
    const cube = cubeService.getOne(req.params.id)[0]
    res.render('details', {cube})
}