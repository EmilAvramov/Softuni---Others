function tickets(array: any[], sort: string) {
	class Ticket {
		destination: string;
		price: number;
		status: string;

		constructor(destination: string, price: number, status: string) {
			this.destination = destination;
			this.price = price;
			this.status = status;
		}
	}

	const data: any[] = [];
	array.forEach((el) => {
		let destination: string, price: number, status: string;
		[destination, price, status] = el.split('|');
		data.push(new Ticket(destination, price, status));
	});
	console.log(
		data.sort(function (a, b) {
			if (a[sort] < b[sort]) {
				return -1;
			}
			if (a[sort] > b[sort]) {
				return 1;
			}
			return 0;
		})
	);
}

tickets(
	[
		'Philadelphia|94.20|available',

		'New York City|95.99|available',

		'New York City|95.99|sold',

		'Boston|126.20|departed',
	],

	'destination'
);
