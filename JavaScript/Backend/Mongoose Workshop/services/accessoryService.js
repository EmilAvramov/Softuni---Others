const Accessory = require('../models/accessory');

exports.create = (accessory) => Accessory.create(accessory);

exports.getAll = async () => Accessory.find();

exports.filter = (ids) => Accessory.find({ _id: {$nin: ids} });
