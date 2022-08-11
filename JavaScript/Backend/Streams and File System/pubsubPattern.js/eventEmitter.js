const EventEmitter = require('events');

const eventEmitter = new EventEmitter()


eventEmitter.on('sing', (title) => {
    console.log(`${title} - lalala`)
})

eventEmitter.emit('sing', 'nothing else matters')