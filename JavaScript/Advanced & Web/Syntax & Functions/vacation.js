function vacation(people, type, day) {
	function discount(price, people, type, prices) {
		if (people >= 30 && type === "Students") {
			return price * 0.85;
		} else if (people >= 100 && type === "Business") {
            price = prices[type][day] * (people - 10)
			return price;
		} else if (people >= 10 && people <= 20 && type === "Regular") {
			return price * 0.95;
		} else {
			return price;
		}
	}

	const prices = {
		Students: {
			Friday: 8.45,
			Saturday: 9.8,
			Sunday: 10.46,
		},
		Business: {
			Friday: 10.9,
			Saturday: 15.6,
			Sunday: 16,
		},
		Regular: {
			Friday: 15,
			Saturday: 20,
			Sunday: 22.5,
		},
	};

	let subTotal = prices[type][day] * people;
	let total = discount(subTotal, people, type, prices);
	console.log(`Total price: ${total.toFixed(2)}`);
}

vacation(30, 'Students', 'Sunday');
vacation(40, 'Regular', 'Saturday');
