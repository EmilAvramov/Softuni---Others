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
var Melon = /** @class */ (function () {
	function Melon(weight, melonSort) {
		this.weight = weight;
		this.melonSort = melonSort;
		this.elementIndex = this.weight = this.melonSort.length;
	}
	Melon.prototype.getElementIndex = function () {
		return this.elementIndex;
	};
	Melon.prototype.toString = function () {
		return 'Element: '
			.concat(this.melonSort, '\nSort: ')
			.concat(this.melonSort, '\nElement Index: ')
			.concat(this.elementIndex);
	};
	return Melon;
})();
var Watermelon = /** @class */ (function (_super) {
	__extends(Watermelon, _super);
	function Watermelon(weight, melonSort) {
		return _super.call(this, weight, melonSort) || this;
	}
	return Watermelon;
})(Melon);
var Firemelon = /** @class */ (function (_super) {
	__extends(Firemelon, _super);
	function Firemelon(weight, melonSort) {
		return _super.call(this, weight, melonSort) || this;
	}
	return Firemelon;
})(Melon);
var Earthmelon = /** @class */ (function (_super) {
	__extends(Earthmelon, _super);
	function Earthmelon(weight, melonSort) {
		return _super.call(this, weight, melonSort) || this;
	}
	return Earthmelon;
})(Melon);
var Airmelon = /** @class */ (function (_super) {
	__extends(Airmelon, _super);
	function Airmelon(weight, melonSort) {
		return _super.call(this, weight, melonSort) || this;
	}
	return Airmelon;
})(Melon);
var Melolemonmelon = /** @class */ (function (_super) {
	__extends(Melolemonmelon, _super);
	function Melolemonmelon(weight, melonSort) {
		var _this = _super.call(this, weight, melonSort) || this;
		_this.elements = [Firemelon, Earthmelon, Airmelon, Watermelon];
		return _this;
	}
	Melolemonmelon.prototype.morph = function () {
		var currentClass = this.elements.shift();
		this.elements.push(currentClass);
		return currentClass;
	};
	return Melolemonmelon;
})(Watermelon);
var test = new Melon(100, 'Test');
var watermelon = new Watermelon(12.5, 'Kingsize');
console.log(watermelon.toString());
