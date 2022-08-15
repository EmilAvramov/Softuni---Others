exports.modelValidator = (Model) => async (req, res, next) => {
	try {
		await Model.validate(req.body);
		next();
	} catch (e) {
		res.status(400).send(Object.values(e)[0]);
	}
};
