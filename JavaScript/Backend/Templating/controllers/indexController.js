const cubes = require('./../config/database.json')

exports.view = (req, res) => {
    res.render('index', {cubes})
}