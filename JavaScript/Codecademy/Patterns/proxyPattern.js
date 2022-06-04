const target = {
    city1: "Marseille, France",
    city2: "Mombasa, Kenya"
};
 
const handler = {
    get: function (target, prop, receiver) {
        if (prop === "city1") {
            return "Montreal, Canada";
        }
        return Reflect.get(...arguments);
    },
};
 
const proxy = new Proxy(target, handler);
 
console.log(proxy.city1); // Montreal, Canada
console.log(proxy.city2); // Mombasa, Kenya