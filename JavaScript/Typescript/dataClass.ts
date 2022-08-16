interface IData {
	method: String;
	uri: String;
	version: String;
	message: String;
}

class Data {
	response: undefined = undefined;
	fulfilled: Boolean = false;

	constructor(
		public method: String,
		public uri: String,
		public version: String,
		public message: String
	) {}
}

let dataUnit: IData = {
	method: 'POST',
	uri: 'site.com',
	version: '1',
	message: 'Hello',
};

let myData = new Data('GET', 'http://google.com', 'HTTP/1.1', 'A message');
console.log(myData);
