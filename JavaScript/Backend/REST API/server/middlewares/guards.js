module.exports = {
	isAuth: () => (req, res, next) => {
		if (req.user) {
			next();
		} else {
			res.status(401).json({ message: 'Please login' });
		}
	},
	isOwner: () => (req, res, next) => {
		if (!req.user) {
			res.status(401).json({ message: 'Please login' });
		} else if (req.user._id == res.locals.item._ownerId) {
			next();
		} else {
			res.status(403).json({message: 'You cannot modify this record'})
		}
	},
};
