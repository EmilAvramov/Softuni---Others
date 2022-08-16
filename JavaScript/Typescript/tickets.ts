function tickets(array: string[], sort: string) {
	class Ticket {
		constructor(
			public destination: string,
			public price: string,
			private status: string
		) {}
		getStatus(): string {
			return this.status;
		}
	}

	const data: object[] = [];
	array.forEach((el) => {
		let destination: string, price: string, status: string;
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
