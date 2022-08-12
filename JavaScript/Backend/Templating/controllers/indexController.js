const cubes = require('./../config/database.json')

exports.index = (req, res) => {
    res.render('index', {cubes})
}