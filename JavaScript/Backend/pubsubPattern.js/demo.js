const eventBus = require('./eventBus');

eventBus.subscribe('say hello', (name, second) =>
	console.log('event say hello executed ' + name + ' ' + second)
);
eventBus.subscribe('say hello', (name, second) =>
	console.log('event say hello executed ' + name + ' ' + second)
);

eventBus.subscribe('say goodbye', (name) => console.log('say bye ' + name));
eventBus.publish('say goodbye', 'gosho');

eventBus.publish('say hello', 'pesho', 'ivan');
eventBus.publish('say-hello', 'Stamat', 'Maria')
