exports.view = (req, res) => {
    let id = req.path.split("/")[2]
    res.render('details', {id})
}