(function () {
    String.prototype.ensureStart = function (n) {
        if (this.startsWith(n) === false) {
            return n + this;
        } else {
            return this + "";
        }
    };
    String.prototype.ensureEnd = function (n) {
        if (this.endsWith(n) === false) {
            return this + n;
        } else {
            return this + "";
        }
    };

    String.prototype.isEmpty = function () {
        return this.length === 0
    };

    String.prototype.truncate = function (n) {
        if (this.length < n) {
          return this + "";
        }
        let value = this; 
        
        while (value.length > n) {
          const index = value.lastIndexOf(" ");
          if (index > -1) {
            value = value.slice(0, index) + "...";
          } else {
            value = n >= 4 ? this.slice(0, n - 3) + "..." : ".".repeat(n);
          }
        }
        return value + "";
      };

    String.format = function (str, ...params) {
        const regex = /{([0-9]+)}/;
        let match = regex.exec(str);
        while (match != null) {
            if (!params[match[1]]) {
                return str;
            }
            str = str.replace(match[0], params[match[1]]);
            match = regex.exec(str);
        }
        return str;
    };
})()

let str = "my string";
str = str.ensureStart("my");
console.log(str);
str = str.ensureStart("hello ");
console.log(str);
str = str.truncate(16);
console.log(str);
str = str.truncate(14);
console.log(str);
str = str.truncate(8);
console.log(str);
str = str.truncate(4);
console.log(str);
str = str.truncate(2);
console.log(str);
str = String.format("The {0} {1} fox", "quick", "brown");
console.log(str);
str = String.format("jumps {0} {1}", "dog");

console.log(str);
