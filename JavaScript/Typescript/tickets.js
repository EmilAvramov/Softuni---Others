function tickets(array, sort) {
    var Ticket = /** @class */ (function () {
        function Ticket(destination, price, status) {
            this.destination = destination;
            this.price = price;
            this.status = status;
        }
        return Ticket;
    }());
    var data = [];
    array.forEach(function (el) {
        var _a;
        var destination, price, status;
        _a = el.split('|'), destination = _a[0], price = _a[1], status = _a[2];
        data.push(new Ticket(destination, price, status));
    });
    console.log(data.sort(function (a, b) {
        if (a[sort] < b[sort]) {
            return -1;
        }
        if (a[sort] > b[sort]) {
            return 1;
        }
        return 0;
    }));
}
tickets([
    'Philadelphia|94.20|available',
    'New York City|95.99|available',
    'New York City|95.99|sold',
    'Boston|126.20|departed',
], 'destination');
