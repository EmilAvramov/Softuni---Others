const mongoose = require('mongoose')

const accessorySchema = new mongoose.Schema({
    id: mongoose.Types.ObjectId,
    name: {
        type:String,
        required: [true, 'This field is required']
    },
    imageUrl: {
		type: String,
		required: [true, 'This field is required'],
	},
    description: {
        type: String,
        required: [true, 'This field is required'],
        maxLength: 120,
    },
    // cubes: {
        
    // }

})

accessorySchema.path('imageUrl').validate(function () {
	return this.imageUrl.startsWith('http');
}, 'Image url should be a link');


const Accessory = mongoose.model('Accessory', accessorySchema)

module.exports = Accessory