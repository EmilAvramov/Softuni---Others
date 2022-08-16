var __extends =
	(this && this.__extends) ||
	(function () {
		var extendStatics = function (d, b) {
			extendStatics =
				Object.setPrototypeOf ||
				({ __proto__: [] } instanceof Array &&
					function (d, b) {
						d.__proto__ = b;
					}) ||
				function (d, b) {
					for (var p in b)
						if (Object.prototype.hasOwnProperty.call(b, p))
							d[p] = b[p];
				};
			return extendStatics(d, b);
		};
		return function (d, b) {
			if (typeof b !== 'function' && b !== null)
				throw new TypeError(
					'Class extends value ' +
						String(b) +
						' is not a constructor or null'
				);
			extendStatics(d, b);
			function __() {
				this.constructor = d;
			}
			d.prototype =
				b === null
					? Object.create(b)
					: ((__.prototype = b.prototype), new __());
		};
	})();
var Employee = /** @class */ (function () {
	function Employee(name, age, salary, tasks) {
		if (salary === void 0) {
			salary = 0;
		}
		if (tasks === void 0) {
			tasks = [];
		}
		this.name = name;
		this.age = age;
		this.salary = salary;
		this.tasks = tasks;
	}
	Employee.prototype.work = function () {
		console.log(this.tasks[0]);
		var temp = '';
		this.tasks = this.tasks.splice(0, 1);
		this.tasks.push(temp);
	};
	Employee.prototype.collectSalary = function () {
		console.log(
			''.concat(this.name, ' received ').concat(this.getSalary())
		);
	};
	Employee.prototype.getSalary = function () {
		return this.salary;
	};
	return Employee;
})();
var Junior = /** @class */ (function (_super) {
	__extends(Junior, _super);
	function Junior(name, age) {
		var _this = _super.call(this, name, age) || this;
		_this.tasks = [''.concat(name, ' is working on a simple task.')];
		return _this;
	}
	return Junior;
})(Employee);
var Senior = /** @class */ (function (_super) {
	__extends(Senior, _super);
	function Senior(name, age) {
		var _this = _super.call(this, name, age) || this;
		_this.tasks = [
			''.concat(name, ' is working on a complicated task.'),
			''.concat(name, ' is taking time off work.'),
			''.concat(name, ' is supervising junior workers.'),
		];
		return _this;
	}
	return Senior;
})(Employee);
var Manager = /** @class */ (function (_super) {
	__extends(Manager, _super);
	function Manager(name, age, dividend) {
		if (dividend === void 0) {
			dividend = 0;
		}
		var _this = _super.call(this, name, age) || this;
		_this.dividend = dividend;
		_this.tasks = [
			''.concat(name, ' scheduled a meeting.'),
			''.concat(name, ' is preparing a quarterly report.'),
		];
		return _this;
	}
	Manager.prototype.getSalary = function () {
		return this.getSalary() + this.dividend;
	};
	return Manager;
})(Employee);
