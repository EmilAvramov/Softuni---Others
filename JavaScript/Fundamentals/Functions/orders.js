function orders(product, qty) {
  const allProducts = {
    coffee: 1.5,
    water: 1.0,
    coke: 1.4,
    snacks: 2,
  };
  if (product in allProducts) {
    console.log((allProducts[product] * qty).toFixed(2));
  }
}

orders("water", 5);
orders("coffee", 2);
