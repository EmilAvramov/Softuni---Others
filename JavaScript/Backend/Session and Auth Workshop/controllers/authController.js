const authService = require('../services/authService')

exports.registerView = (req, res) => {
    res.render('auth/register')
}

exports.registerPost = (req, res) => {
    authService.register(req.body)
    res.redirect('/')
}

exports.loginView = (req, res) => {
    res.render('auth/login')
}

exports.loginPost = (req, res) => {
    console.log(req.body)
    res.redirect('/')
}

exports.logout = (req, res) => {
    res.redirect('/')
}